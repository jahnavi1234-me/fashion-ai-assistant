from src.data_loader import DataLoader
from src.compatibility_engine import CompatibilityEngine


class FashionRecommender:

    def __init__(self):
        loader = DataLoader()
        self.outfits_df, self.products_df = loader.load_all()

        self.engine = CompatibilityEngine(self.outfits_df)

    def recommend_outfit(self, gender, occasion, wear_type):

        results = self.engine.recommend(gender, occasion, wear_type)

        return [
            self.engine.get_complete_outfit(row)
            for _, row in results.iterrows()
        ]