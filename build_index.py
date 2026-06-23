from src.data_loader import DataLoader
from src.embedding_generator import EmbeddingGenerator
from src.faiss_store import FaissStore


def build_index():

    print("🚀 Loading data...")

    loader = DataLoader()
    outfits_df, _ = loader.load_all()

    print(f"Loaded {len(outfits_df)} outfits")

    print("🧠 Initializing embedding model...")
    embedder = EmbeddingGenerator()

    print("📦 Initializing FAISS store...")
    store = FaissStore()

    for idx, row in outfits_df.iterrows():

        # 🧾 Create text representation of outfit
        text = f"""
        {row['hero']} {row['second']} {row['layer']}
        {row['footwear']} {row['accessory_1']} {row['accessory_2']}
        {row['stylist_rationale']}
        """

        # 🔥 Generate embedding
        vector = embedder.generate_text_embedding(text)

        # 📌 Metadata for retrieval
        metadata = {
            "hero": row["hero"],
            "second": row["second"],
            "layer": row["layer"],
            "footwear": row["footwear"],
            "accessory_1": row["accessory_1"],
            "accessory_2": row["accessory_2"],
            "reason": row["stylist_rationale"],
            "image_url": row.get("image_url", None)
        }

        # ➕ Add to FAISS
        store.add_vector(vector, metadata)

        print(f"Indexed {idx + 1}/{len(outfits_df)}")

    print("💾 Saving FAISS index...")
    store.save()

    print("✅ Build complete!")


if __name__ == "__main__":
    build_index()