import streamlit as st
from genai_bot import GenAIBot
from recommender import MovieRecommender

# --- INIT ---
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")
st.title("🎬 Smart Movie Recommender with Gemini AI")

# Get API key securely (optional: use secrets.toml)
API_KEY = "AIzaSyAGOP32zUkSX2Pi5GIrk87Bad8w0q9-Ixg "  # Replace this with your actual key

# Initialize bots
genai_bot = GenAIBot(API_KEY)
recommender = MovieRecommender()

# --- CHATBOX ---
user_input = st.text_input("What kind of movie are you in the mood for?", placeholder="e.g., I want something nostalgic and funny")

if st.button("🎥 Recommend"):
    if user_input.strip():
        # Rule-based suggestions (try genre filtering)
        genres = ["Romance", "Comedy", "Action", "Horror", "Sci-Fi", "Animation"]
        matches = [genre for genre in genres if genre.lower() in user_input.lower()]
        
        if matches:
            recs = []
            for genre in matches:
                recs.extend(recommender.recommend_by_genre(genre))
            if recs:
                st.success("🎯 Recommendations based on genre:")
                for r in recs:
                    st.markdown(f"- {r}")
            else:
                st.warning("No matches found in local dataset.")
        else:
            # Fall back to Gemini AI
            ai_response = genai_bot.get_reply(f"Suggest movies. The user said: {user_input}")
            st.info("🤖 Gemini's recommendation:")
            st.write(ai_response)
    else:
        st.warning("Please type something first.")
