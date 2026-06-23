# embedding_generator.py

import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


class EmbeddingGenerator:

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model = CLIPModel.from_pretrained(
            "openai/clip-vit-base-patch32"
        ).to(self.device)

        self.processor = CLIPProcessor.from_pretrained(
            "openai/clip-vit-base-patch32"
        )

    def generate_image_embedding(self, image):

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        ).to(self.device)

        with torch.no_grad():
            embedding = self.model.get_image_features(**inputs)

        embedding = embedding.cpu().numpy()[0]

        return embedding

    def generate_text_embedding(self, text):

        inputs = self.processor(
            text=[text],
            return_tensors="pt",
            padding=True
        ).to(self.device)

        with torch.no_grad():
            embedding = self.model.get_text_features(**inputs)

        embedding = embedding.cpu().numpy()[0]

        return embedding