
class Index:
    """
    A base class for the Indices encapsulated by the [`RagRetriever`].
    """

    def get_doc_dicts(self, doc_ids: np.ndarray) -> List[dict]:
        """
        Returns a list of dictionaries, containing titles and text of the retrieved documents.

        Args:
            doc_ids (`np.ndarray` of shape `(batch_size, n_docs)`):
                A tensor of document indices.
        """
        raise NotImplementedError

    def get_top_docs(self, question_hidden_states: np.ndarray, n_docs=5) -> Tuple[np.ndarray, np.ndarray]:
        """
        For each query in the batch, retrieves `n_docs` documents.

        Args:
            question_hidden_states (`np.ndarray` of shape `(batch_size, vector_size)`):
                An array of query vectors.
            n_docs (`int`):
                The number of docs retrieved per query.

        Returns:
            `np.ndarray` of shape `(batch_size, n_docs)`: A tensor of indices of retrieved documents. `np.ndarray` of
            shape `(batch_size, vector_size)`: A tensor of vector representations of retrieved documents.
        """
        raise NotImplementedError

    def is_initialized(self):
        """
        Returns `True` if index is already initialized.
        """
        raise NotImplementedError

    def init_index(self):
        """
        A function responsible for loading the index into memory. Should be called only once per training run of a RAG
        model. E.g. if the model is trained on multiple GPUs in a distributed setup, only one of the workers will load
        the index.
        """
        raise NotImplementedError


class LegacyIndex(Index):

    FILENAME = "somthing.pkl"

    def __init__(self, vector_size, index_path):
        self.index_id_to_db_id = []
        self.index_path = index_path
        self.passages = self._load_passages()
        self.vector_size = vector_size
        self.index = None
        self._index_initialized = False

    def _resolve_path(self, index_path, filename):
        is_local = os.path.isdir(index_path)
        if is_local:
            return os.path.join(index_path, filename)
        else:
            raise ValueError(f"Index path {index_path} is not a directory.")

    def _load_passages(self):
        passages_path = self._resolve_path(self.index_path, self.FILENAME)
        with open(passages_path, "rb") as passages_file:
            passages = pickle.load(passages_file)
        return passages

    def _deserialize_index(self):
        # prepare index
        resolved_index_path = self._resolve_path(self.index_path, self.FILENAME)
        self.index = faiss.read_index(resolve_index_path)
        resolved_meta_patch = self._resolve_path(self.index_path, "meta.json")
        with open(resolved_meta_patch, "rb") as meta_file:
            self.index_id_to_db_id = pickle.load(meta_file)

        assert len(self.index_id_to_db_id) == self.index.ntotal

    def is_initialized(self):
        return self._index_initialized

    def init_index(self):
        index = faiss.IndexHNSWFlat(self.vector_size + 1, 512)
        index.hnsw.efSearch = 128
        index.hnsw.efConstruction = 200
        self.index = index
        self._deserialize_index()
        self._index_initialized = True

    def get_doc_dicts(self, doc_ids: np.ndarray) -> List[dict]:
        doc_list = []
        for doc_ids_i in doc_ids:
            ids = [str(int(doc_id)) for doc_id in doc_ids_i]
            docs = [self.passages[doc_id] for doc_id in ids]
            doc_list.append(docs)

        doc_dicts = []
        for docs in doc_list:
            doc_dict = {}
            doc_dict["title"] = [doc[0] for doc in docs]
            doc_dict["text"] = [doc[1] for doc in docs]
            doc_dicts.append(doc_dict)

        return doc_dicts

    def get_top_docs(
        self,
        target_hidden_states: np.ndarray,
        n_docs=5,
    ) -> Tuple[np.ndarray, np.ndarray]:
        aux_dim = np.zeros(len(target_hidden_states), dtype=np.float32).reshape(-1, 1)
        target_nhsw_vectors = np.hstack((target_hidden_states, aux_dim))
        _, docs_ids = self.index.search(target_nhsw_vectors, n_docs)
        vectors = [[self.index.reconstruct(int(doc_id))[:-1] for doc_id in doc_ids] for doc_ids in docs_ids]
        ids = [[int(self.index_id_to_db_id[doc_id]) for doc_id in doc_ids] for doc_ids in docs_ids]

        return np.array(ids), np.array(vectors)


class REHLRetriever:
    
    def __init__(
        self,
        config,
        target_encoder_tokenizer,
        highlighter_tokenizer,
        index=None,
        init_retrieval=True,
    ):

        self._init_retrieval = init_retrieval
        self.index = index or self._build_index(config)
        self.target_encoder_tokenizer = target_encoder_tokenizer
        self.highlighter_tokenizer = highlighter_tokenizer

        self.n_docs = config.n_docs
        self.batch_size = config.retrieval_batch_size
        self.config = config

        if self._init_retrieval:
            self.index.init_index()

        self.ctx_encoder_tokenizer = None
        self.return_tokenzied_docs = False
        
    @staticmethod
    def _build_index(config):
        return LegacyIndex(config.vector_size, config.index_path)


    @classmethod
    def from_pretrained(
        cls, 
        retriever_name_or_path, 
        target_encoder_name_or_path,
        highlighter_name_or_path,
        indexed_dataset=None, **kwargs
    ):
        config = kwargs.pop("config", None) or AutoConfig.from_pretrained(retriever_name_or_path, **kwargs)
        retriever_tokenizer = AutoTokenizer.from_pretrained(retriever_name_or_path, config=config)
        target_encoder_tokenizer = AutoTokenizer.from_pretrained(target_encoder_name_or_path)
        highlighter_tokenizer = AutoTokenizer.from_pretrained(highlighter_name_or_path)
        if indexed_dataset is not None:
            config.index_path = indexed_dataset
            index = LegacyIndex(config.vector_size, config.index_path)
        else:
            index = cls._build_index(config)

        return cls(config, target_encoder_tokenizer, highlighter_tokenizer, index=index, **kwargs)
        

