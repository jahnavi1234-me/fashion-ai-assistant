from src.faiss_store import FaissStore


class FaissSearch:

    def __init__(self):

        self.store = FaissStore()
        self.store.load()

    def search(self, embedding):

        return self.store.search(
            embedding,
            top_k=5
        )