from retriever.base import BaseRetriever


class DPRRetriever(BaseRetriever):
    def __init__(self, config):
        super(DPRRetriever, self).__init__(config)

    def retrieve(self, query):
        return self._retrieve(query)

    def _retrieve(self, query):
        raise NotImplementedError
