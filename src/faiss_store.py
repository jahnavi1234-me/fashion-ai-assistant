import faiss
import numpy as np
import pickle


class FaissStore:

    def __init__(
        self,
        dimension=512,
        index_path="vector_db/faiss_index.bin",
        metadata_path="vector_db/metadata.pkl"
    ):
        self.dimension = dimension
        self.index_path = index_path
        self.metadata_path = metadata_path

        self.index = faiss.IndexFlatL2(dimension)
        self.metadata = []

    def add_vector(self, vector, metadata):

        vector = np.array(vector, dtype=np.float32).reshape(1, -1)

        self.index.add(vector)
        self.metadata.append(metadata)

    def save(self):

        faiss.write_index(self.index, self.index_path)

        with open(self.metadata_path, "wb") as f:
            pickle.dump(self.metadata, f)

    def load(self):

        self.index = faiss.read_index(self.index_path)

        with open(self.metadata_path, "rb") as f:
            self.metadata = pickle.load(f)

    def search(self, query_vector, top_k=5):

        query_vector = np.array(query_vector, dtype=np.float32).reshape(1, -1)

        _, indices = self.index.search(query_vector, top_k)

        return [
            self.metadata[i]
            for i in indices[0]
            if i < len(self.metadata)
        ]