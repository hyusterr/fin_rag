


class End2EndREHighlighter:
    def __init__(
        self,
        query_encoder,
        retriever,
        highlighter,
        **kwargs
    ):
        self.query_encoder = query_encoder
        self.retriever = retriever
        self.highlighter = highlighter

    def foward(
        self,
        input_ids, 
        attention_mask,
        encoder_outputs,
        doc_scores,
        context_input_ids,
        context_attention_mask,
        context_encoder_training,
        output_attentions,
        output_hidden_states,
        output_retrieved,
        n_docs,
        true_labels,
    ):

        has_to_retrieve = (
            self.retriever is not None
            and encoder_outputs is not None
            and (doc_scores is None or context_input_ids is None or context_attention_mask is None)
        )

        if encoder_outputs is None:
            target_enc_outputs = self.query_encoder(
                input_ids=input_ids,
                attention_mask=attention_mask,
                return_dict=True,
            )
            target_encoder_last_hidden_state = target_enc_outputs.last_hidden_state

        if has_to_retrieve:
            retriever_outputs = self.retriever(
                input_ids,
                target_encoder_last_hidden_state.cpu().detach().to(torch.float32).numpy(),
                n_docs=n_docs,
                return_tensors="pt",
            )

            if not context_encoder_training:
                context_input_ids = retriever_outputs["context_input_ids"]
                context_attention_mask = retriever_outputs["context_attention_mask"]
                retrieved_doc_embeds = retriever_outputs["retrieved_doc_embeds"]
                retrieved_doc_ids = retriever_outputs["doc_ids"]

                # send to correct device as encoder_outputs
                retrieved_doc_embeds = retrieved_doc_embeds.to(target_encoder_last_hidden_state)
                context_input_ids = context_input_ids.to(input_ids)
                context_attention_mask = context_attention_mask.to(attention_mask)

                doc_scores = torch.bmm(
                    target_encoder_last_hidden_state.unsqueeze(1),
                    retrieved_doc_embeds.transpose(1, 2),
                ).squeeze(1)


            else:
                pass
                # TODO: Implement training of the context encoder

        # assertions: if tensors not get from forward, they should be passed as arguments
        assert doc_scores is not None, "doc_scores should be passed as argument"
        assert context_input_ids is not None, "context_input_ids should be passed as argument"
        assert context_attention_mask is not None, "context_attention_mask should be passed as argument"
        # assertions: assert the shape of doc_scores is correct
        assert doc_scores.shape[1] % n_docs == 0, "The number of documents in doc_scores should be divisible by n_docs"

        highlighter_outputs = self.highlighter(
            target_input_ids=input_ids,
            target_attention_mask=attention_mask,
            context_input_ids=context_input_ids,
            context_attention_mask=context_attention_mask,
            doc_scores=doc_scores,
            output_attentions=output_attentions,
            output_hidden_states=output_hidden_states,
        )

        marginalized_logits = self.marginialize(
            target_logits=highlighter_outputs.logits,
            doc_scores=doc_scores,
            n_docs=n_docs,
        )

        loss = None
        if true_labels is not None:
            loss = F.cross_entropy(marginalized_logits, true_labels)

        return {
            "loss": loss,
            "logits": marginalized_logits,
            "doc_scores": doc_scores,
            "context_input_ids": context_input_ids,
            "context_attention_mask": context_attention_mask,
            "retrieved_doc_ids": retrieved_doc_ids,
            "retrieved_doc_embeds": retrieved_doc_embeds,
            "encoder_outputs": target_enc_outputs,
            "highlighter_outputs": highlighter_outputs,
        }

    def highight(
        self,
        input_ids,
        attention_mask,
        context_input_ids,
        context_attention_mask,
        doc_scores,
        output_attentions=False,
        output_hidden_states=False,
    ):
        # need to marginalize the doc_scores to get the scores for each token
        pass
            

    def marginalize(
        self,
        target_logits,
        doc_scores,
        n_docs,
    ):
        assert doc_scores.shape[1] % n_docs == 0, "The number of documents in doc_scores should be divisible by n_docs"
        doc_scores = doc_scores.view(-1, n_docs)
        doc_scores = doc_scores.softmax(dim=-1)
        target_logits = target_logits.unsqueeze(1)
        target_logits = target_logits * doc_scores

        return target_logits






