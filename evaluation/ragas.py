# https://arxiv.org/pdf/2309.15217v1.pdf
'''
RAGAs contains 3 metrics:
1. faithfulness
2. answer relevance
3. context relevance
    - concept: The context c(q) is considered relevant to the extent that it exclusively contains information that is needed to answer the question. In particular, this metric aims to penalise the inclusion of redundant information.
    - original prompt: Please extract relevant sentences from the provided context that can potentially help answer the following question. If no relevant sentences are found, or if you believe the question cannot be answered from the given context, return the phrase "Insufficient Information". While extracting candidate sentences you’re not allowed to make any changes to sentences from given context.
    - formula: The context relevance score is then computed as: CR = number of extracted sentences / total number of sentences in c(q)
'''

# use mistral or llama3, instruct version to implement it
# be aware of different preprocessing like [INST] [/INST]...
