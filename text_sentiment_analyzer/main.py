from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:     
        return "Positive"
    elif sentiment < 0:
        return "Negative"
    else:
        return "Neutral"

# text = "I love Python programming!"
# print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")

def analyze_sentiment_vader(text):
    sentiment_scores = analyzer.polarity_scores(text)['compound']
    if sentiment_scores >= 0.05:
        return "Positive"
    elif sentiment_scores <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# text = "I love Python programming!"
# print(f"VADER Sentiment: {analyze_sentiment_vader(text)}")

def analyze_user_input():
    while True:
        text = input("Enter text for sentiment analysis (or 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting sentiment analysis.")
            break
        print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
        print(f"VADER Sentiment: {analyze_sentiment_vader(text)}")

analyze_user_input()