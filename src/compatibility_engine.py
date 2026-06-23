class CompatibilityEngine:

    def __init__(self, outfits_df):
        self.outfits_df = outfits_df

    def recommend(self, gender=None, occasion=None, wear_type=None):

        df = self.outfits_df.copy()

        if gender:
            df = df[df["gender"].str.lower() == gender.lower()]

        if occasion:
            df = df[df["occasion"].str.lower() == occasion.lower()]

        if wear_type:
            df = df[df["wear_type"].str.lower() == wear_type.lower()]

        return df.head(5)

    def get_complete_outfit(self, row):

        return {
            "hero": row["hero"],
            "second": row["second"],
            "layer": row["layer"],
            "footwear": row["footwear"],
            "accessory_1": row["accessory_1"],
            "accessory_2": row["accessory_2"],
            "reason": row["stylist_rationale"],
            "image_urls": row["image_urls"]
        }