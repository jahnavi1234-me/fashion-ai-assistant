# image_loader.py

import os
from PIL import Image


class ImageLoader:
    def __init__(self, image_root="data/images"):
        self.image_root = image_root

    def load_image(self, image_path):
        """
        Load a single image.
        Example:
        images/ajio/703182002.jpg
        """
        full_path = image_path

        if not os.path.exists(full_path):
            print(f"Image not found: {full_path}")
            return None

        try:
            image = Image.open(full_path).convert("RGB")
            return image
        except Exception as e:
            print(f"Error loading image {full_path}: {e}")
            return None

    def load_multiple_images(self, image_paths):
        images = []

        for path in image_paths:
            image = self.load_image(path)

            if image is not None:
                images.append(image)

        return images

    def parse_outfit_images(self, image_files):
        """
        image_files column example:
        images/ajio/703182002.jpg;
        images/myntra/42540276.jpg;
        images/myntra/15660676.jpg
        """

        if not isinstance(image_files, str):
            return []

        paths = [img.strip() for img in image_files.split(";")]

        return self.load_multiple_images(paths)


if __name__ == "__main__":

    loader = ImageLoader()

    sample = (
        "images/ajio/703182002.jpg;"
        "images/myntra/42540276.jpg;"
        "images/myntra/15660676.jpg"
    )

    images = loader.parse_outfit_images(sample)

    print(f"Loaded {len(images)} images")