# llm_handler.py

import google.generativeai as genai


class LLMHandler:

    def __init__(self, api_key):

        genai.configure(
            api_key=api_key
        )

        self.model = genai.GenerativeModel(
            "gemini-1.5-flash"
        )

    def explain_outfit(
        self,
        user_query,
        outfit
    ):

        prompt = f"""
        User Request:
        {user_query}

        Outfit:
        {outfit}

        Explain why this outfit is suitable.

        Keep explanation under 100 words.
        """

        response = self.model.generate_content(
            prompt
        )

        return response.text