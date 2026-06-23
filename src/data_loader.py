import pandas as pd
import os


class DataLoader:

    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))

        self.outfits_path = os.path.join(base_dir, "ML-TASK", "outfits.csv")
        self.products_path = os.path.join(base_dir, "ML-TASK", "products.csv")

        self.base_url = "https://raw.githubusercontent.com/DarexAI-AI-Startup/ML-TASK/main/"

    def process_images(self, img_str):

        if not isinstance(img_str, str) or img_str == "None":
            return []

        paths = img_str.split(";")

        return [self.base_url + p.strip() for p in paths]

    def load_outfits(self):

        df = pd.read_csv(self.outfits_path).fillna("None")

        df["image_urls"] = df["image_files"].apply(self.process_images)

        return df

    def load_products(self):

        df = pd.read_csv(self.products_path).fillna("None")

        if "image" in df.columns:
            df["image_url"] = df["image"].apply(
                lambda x: self.base_url + x if x != "None" else None
            )

        return df

    def load_all(self):
        return self.load_outfits(), self.load_products()