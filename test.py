from utils.utils import retrieve_paragraph_from_docid
from highlighter.cnc_highlighter import CncBertHighlighter
from highlighter.attn_highlighter import AttnHighlighter


if __name__ == "__main__":
    reference_docids = [
        "20221028_10-K_320193_part2_item7_para7",
        "20221028_10-K_320193_part2_item7_para8",
        "20220318_10-K_1045810_part2_item7_para5"
    ]
    text_references = [retrieve_paragraph_from_docid(docid) for docid in reference_docids]
    target = retrieve_paragraph_from_docid("20221028_10-K_320193_part2_item7_para7")
    # highlighter = CncBertHighlighter()
    # highlighter = AttnHighlighter(device='cuda:1')
    # highlighter = AttnHighlighter('Sigma/financial-sentiment-analysis', 'text-classification', 'cuda:1')
    # highlighter = AttnHighlighter('ahmedrachid/FinancialBERT-Sentiment-Analysis', 'text-classification', 'cuda:1')
    highlighter = AttnHighlighter('mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis', 'text-classification', 'cuda:1')
    highlight_results = highlighter.highlighting_outputs(target, text_references, mean_aggregate=True, label_threshold=0.3, generate_spans=True)
    # highlighter.visualize_top_k_highlight(highlight_results, highlight_words_cnt=5)
    print(highlight_results)
