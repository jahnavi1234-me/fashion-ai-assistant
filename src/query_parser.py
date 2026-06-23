class QueryParser:

    def parse(self, query):

        q = query.lower()

        result = {
            "gender": None,
            "occasion": None,
            "wear_type": "western"
        }

        if "men" in q or "male" in q:
            result["gender"] = "men"
        elif "women" in q or "female" in q:
            result["gender"] = "women"

        occasions = [
            "casual", "party", "office", "wedding",
            "vacation", "sports", "festive", "winter"
        ]

        for occ in occasions:
            if occ in q:
                result["occasion"] = occ

        if "ethnic" in q:
            result["wear_type"] = "ethnic"

        return result