import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import streamlit as st
from recommender import FashionRecommender
from src.query_parser import QueryParser


st.set_page_config(page_title="AI Fashion Assistant", layout="wide")

st.title("👔 AI Fashion Assistant")

query = st.text_input("Describe your outfit requirement")

if st.button("Recommend Outfit"):

    parser = QueryParser()
    parsed = parser.parse(query)

    recommender = FashionRecommender()

    results = recommender.recommend_outfit(
        parsed["gender"],
        parsed["occasion"],
        parsed["wear_type"]
    )

    if not results:
        st.warning("No matching outfit found")

    else:

        for outfit in results:

            st.subheader("Recommended Outfit")

            # 🖼️ MULTI IMAGE SUPPORT
            images = outfit.get("image_urls", [])

            if images:
                cols = st.columns(len(images))
                for i, img in enumerate(images):
                    with cols[i]:
                        st.image(img)

            st.write("Topwear:", outfit["hero"])
            st.write("Bottomwear:", outfit["second"])
            st.write("Layer:", outfit["layer"])
            st.write("Footwear:", outfit["footwear"])
            st.write("Accessory 1:", outfit["accessory_1"])
            st.write("Accessory 2:", outfit["accessory_2"])

            st.success(outfit["reason"])