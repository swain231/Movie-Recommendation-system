import google.generativeai as genai

class GenAIBot:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name="models/chat-bison-001")

    def get_reply(self, prompt):
        response = self.model.generate_content(prompt)
        return response.text.strip()

