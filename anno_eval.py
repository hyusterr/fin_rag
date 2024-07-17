# evaluate the annotation quality of the dataset
from annotation.aggregatew_annotation import read_jsonl, TOPIC_MAP, SUBTOPIC_MAP, TYPE_MAP

def preprocess_sample(sample):
    sample_id = sample['id']
    text = sample['text']
    tokens = text.split()
    binary_labels = [0] * len(tokens)
    signal_type = [k for k, v in sample['type'].items() if v == 1]
    topic = [k for k, v in sample['topic'].items() if v != 0]
    sub_topic = [f'{k}-{v}' for k, v in sample['topic'].items() if v not in [0, 1]]
    if len(sample['highlight']) != 0:
        highlight_spans = sample['highlight'].split(' ||| ')
        span_tokens = [s.strip().split() for s in highlight_spans] # list of list of tokens
        span_tokens = [s for s in span_tokens if len(s) > 0] # filter out empty spans
        
        span_already_checked = 0
        i = 0
        while i < len(tokens):
            if span_alread_checked == len(span_tokens):
                break

            if tokens[i] == span_tokens[span_already_checked][0]:
                if tokens[i:i+len(span_tokens[span_already_checked])] == span_tokens[span_already_checked]:
                    binary_labels[i:i+len(span_tokens[span_already_checked])] = [1] * len(span_tokens[span_already_checked])
                    i += len(span_tokens[span_already_checked])
                    span_already_checked += 1
                else:
                    i += 1
            else:
                i += 1
    
    return {
        sample_id: {
            'text': text,
            'tokens': tokens,
            'binary_labels': binary_labels,
            'signal_type': signal_type,
            'topic': topic,
            'sub_topic': sub_topic
        }
    }

def preprocess_annotations(annotations_files):
    annotations = [read_jsonl(f) for f in annotation_files]
    annotators = [f.split('/')[-1].split('.')[0].split('_')[0] for f in annotation_files]
    sample_size = len(annotations[0])

    annotator_annotations = {a: dict() for a in annotators}
    sample_id_set = set()
    for annotator, annotation in zip(annotators, annotations):
        for sample in annotation:
            preprocessed_sample = preprocess_sample(sample)
            annotator_annotations[annotator].update(preprocessed_sample)
            sample_id_set.add(sample.keys())

    return annotator_annotations, sample_id_set





def evaluate_annotation(annotation_files):
    annotator_annotations, sample_id_set = preprocess_annotations(annotation_files)

    # check for bugs
    for annotator, annotation in annotator_annotations.items():
        # missing samples
        missing_samples = sample_id_set - set(annotation.keys())
        assert len(missing_samples) == 0, f'{annotator} is missing samples: {missing_samples}'
        # extra samples
        extra_samples = set(annotation.keys()) - sample_id_set
        assert len(extra_samples) == 0, f'{annotator} has extra samples: {extra_samples}'

        for sid, sample in annotation.items():
            # check if # of type != 1 
            assert len(sample['signal_type']) == 1, f'{annotator} has multiple signal types in sample {sid}'
            signal_type = TYPE_MAP[sample['signal_type'][0]] if len(sample['signal_type']) == 1
            # check if # of topic != 1
            assert len(sample['topic']) == 1, f'{annotator} has multiple topics in sample {sid}'
            topic = TOPIC_MAP[sample['topic'][0]] if len(sample['topic']) == 1
            # check if # of sub_topic <= 1
            assert len(sample['sub_topic']) <= 1, f'{annotator} has multiple sub_topics in sample {sid}'
            sub_topic = SUBTOPIC_MAP[sample['sub_topic'][0]] if len(sample['sub_topic']) == 1 else None

    sample_id_list = list(sample_id_set)
    # check for agreement
    # inter-annotator agreement, loop over samples
    for id_ in sample_id_list:
        sample_from_annotators = [annotator_annotations[a][id_] for a in annotator_annotations.keys()]
        # strict agreement: all annotators agree on the same label
        # highlights

        # type

    # soft agreement, see: https://en.innovatiana.com/post/inter-annotator-agreement
    # Fleiss' kappa on highlights

    # intra-class correlation on highlights

    # Krippendorff alpha on type

    # Krippendorff alpha on topic

    # intra-annotator agreement
