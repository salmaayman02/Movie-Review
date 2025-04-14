import streamlit as st
import pickle

# Load saved model and vectorizer
with open("sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

# Streamlit UI
st.title("🎬 Movie Review Sentiment Analyzer")
st.markdown("Enter a movie review and find out if it's **positive** or **negative**.")

user_input = st.text_area("Your Review:", height=150)

if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a review first!")
    else:
        input_vector = vectorizer.transform([user_input])
        prediction = model.predict(input_vector)[0]
        emoji = "👍" if prediction == "pos" else "👎"
        st.success(f"**Sentiment:** {prediction.upper()} {emoji}")
