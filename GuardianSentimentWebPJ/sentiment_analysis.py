# sentiment_analysis.py
#This file conducts a sentiment analysis based on textblob

from textblob import TextBlob  # Import TextBlob for sentiment analysis

def analyze_sentiment(text):
    blob = TextBlob(text)  # Create a TextBlob object from the text
    return {
        "polarity": blob.sentiment.polarity,  # Extract polarity score
        "subjectivity": blob.sentiment.subjectivity  # Extract subjectivity score
    }


def analyze_articles(articles):
    # Loop through each article and analyze its text
    for article in articles:
        sentiment = analyze_sentiment(article["text"])  # Analyze the article's text
        article["sentiment"] = sentiment  # Add sentiment (polarity and subjectivity)
        article["subjectivity"] = sentiment["subjectivity"]  # Add subjectivity explicitly

    return articles  # Return the updated list of articles
