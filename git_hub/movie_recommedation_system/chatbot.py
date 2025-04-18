class ChatBot:
    def __init__(self, recommender):
        self.recommender = recommender

    def get_response(self, message):
        message = message.lower()
        if "romance" in message:
            return self.recommender.recommend_by_genre("Romance")
        elif "comedy" in message or "funny" in message:
            return self.recommender.recommend_by_genre("Comedy")
        elif "action" in message:
            return self.recommender.recommend_by_genre("Action")
        elif "horror" in message:
            return self.recommender.recommend_by_genre("Horror")
        elif "sci-fi" in message or "science fiction" in message:
            return self.recommender.recommend_by_genre("Sci-Fi")
        elif "animation" in message or "cartoon" in message:
            return self.recommender.recommend_by_genre("Animation")
        else:
            return ["Please tell me what kind of movie you’d like to watch (e.g., action, romance, comedy)."]
