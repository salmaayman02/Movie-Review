# 🎬Movie Review Sentiment Analyzer

This is a web application that predicts the sentiment of movie reviews as either **positive** or **negative** using a machine learning model. The application is built using Streamlit for the user interface.

## 📌Features

- Analyze the sentiment of any movie review text.
- Instantly get sentiment prediction: Positive (👍) or Negative (👎).
- Simple and intuitive user interface.

## 🧠How It Works

1. The user inputs a movie review in the text box.
2. The review is preprocessed and transformed using a saved `TfidfVectorizer`.
3. The transformed input is passed to a trained machine learning model.
4. The model returns a sentiment prediction: `"pos"` for positive or `"neg"` for negative.

## 🗃️Files

- `app.py`: Main Streamlit application.
- `sentiment_model.pkl`: Trained sentiment classification model (e.g., logistic regression or Naive Bayes).
- `vectorizer.pkl`: Fitted TF-IDF vectorizer used to transform input text.
- `model.ipynb`: Jupyter notebook used for training and evaluating the model.

## Requirements

- Python 3.7 or higher
- Required packages:
  - streamlit
  - scikit-learn
  - pickle (standard library)

## Installation

1. Clone the repository or download the files.
2. Place `sentiment_model.pkl` and `vectorizer.pkl` in the same directory as `app.py`.
3. Install dependencies:
   ```bash
    pip install streamlit scikit-learn
4. Run the application:
   ```bash
    streamlit run app.py




   

