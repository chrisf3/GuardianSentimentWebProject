# data_processing.py
#This file is responsible for the processing of the received data into a useful csv table and preparing it for visualisation and analysis

import pandas as pd  # Import pandas for data processing and CSV handling


def process_articles(articles):
    """
    Process raw article data to extract and structure relevant fields.

    Parameters:
    - articles (list[dict]): List of raw articles fetched from the API.

    Returns:
    - List of processed articles, each represented as a dictionary with key fields.
    """
    processed = []  # List to hold the processed articles

    # Extract relevant fields from each article
    for article in articles:
        processed.append({
            "id": article.get("id"),  # Unique ID for the article
            "webTitle": article.get("webTitle"),  # Article title
            "sectionName": article.get("sectionName"),  # Section/category of the article
            "webUrl": article.get("webUrl"),  # URL to the article
            "text": article.get("fields", {}).get("bodyText", ""),  # Main content of the article
            "publicationDate": article.get("webPublicationDate")  # Publication date
        })

    return processed  # Return the list of processed articles


def save_to_csv(articles, filename):
    """
    Save processed articles to a CSV file.

    Parameters:
    - articles (list[dict]): List of processed articles.
    - filename (str): Path to the output CSV file.

    Returns:
    - None. Saves the data to the specified CSV file.
    """
    # Convert the list of articles to a pandas DataFrame
    df = pd.DataFrame(articles)

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

    # Print a confirmation message
    print(f"Saved {len(articles)} articles to {filename}")