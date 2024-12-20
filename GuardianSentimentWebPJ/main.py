#main.py
#This is the main python file on the backend

import os
from guardian_api import fetch_articles  # Fetch articles from The Guardian API
from data_processing import process_articles, save_to_csv  # Process and save article data
from sentiment_analysis import analyze_articles  # Perform sentiment analysis
from visualization import (  # Generate visualizations
    plot_over_time,
    plot_distribution,
    plot_polarity_vs_subjectivity,
)

# Directory to store generated images and CSV files
STATIC_DIR = "static/images"

def process_keyword_year(keyword, year):
    """
    Main function to fetch, process, analyze, and visualize data dynamically based on inputs.
    - Fetch articles from The Guardian based on a keyword and year.
    - Process and analyze the articles for sentiment and subjectivity.
    - Generate visualizations and save the outputs.
    """
    section = "world"  # Define the section for article search
    max_articles = 1000  # Maximum number of articles to fetch
    moving_average_window = max(1, int(max_articles * 0.05))  # Window size for smoothing trends
    geo = ""  # Placeholder for geographical filtering (unused)

    # Ensure the output directory exists
    os.makedirs(STATIC_DIR, exist_ok=True)

    # Step 1: Fetch articles
    articles = fetch_articles(section=section, keyword=keyword, max_articles=max_articles, year=year)
    if not articles:
        raise ValueError("No articles found for the provided keyword.")  # Handle case where no articles are found

    # Step 2: Process and analyze articles
    processed_articles = process_articles(articles)  # Clean and structure raw article data
    analyzed_articles = analyze_articles(processed_articles)  # Perform sentiment analysis
    save_to_csv(analyzed_articles, os.path.join(STATIC_DIR, "guardian_articles.csv"))  # Save results to CSV

    # Step 3: Generate and save visualizations
    # Trend of polarity over time
    plot_over_time(
        analyzed_articles,
        metric="polarity",
        moving_average_window=moving_average_window,
        save_path=f"{STATIC_DIR}/polarity_over_time.png"
    )

    # Trend of subjectivity over time
    plot_over_time(
        analyzed_articles,
        metric="subjectivity",
        moving_average_window=moving_average_window,
        save_path=f"{STATIC_DIR}/subjectivity_over_time.png"
    )

    # Distribution of polarity values
    plot_distribution(
        analyzed_articles,
        metric="polarity",
        bins=20,
        save_path=f"{STATIC_DIR}/polarity_distribution.png"
    )

    # Distribution of subjectivity values
    plot_distribution(
        analyzed_articles,
        metric="subjectivity",
        bins=20,
        save_path=f"{STATIC_DIR}/subjectivity_distribution.png"
    )

    # Scatter plot of polarity vs. subjectivity
    plot_polarity_vs_subjectivity(
        analyzed_articles,
        save_path=f"{STATIC_DIR}/polarity_vs_subjectivity.png"
    )
