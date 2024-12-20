# Guardian Article Analysis Project

This project is an official submission of the Group Project Work for the course Introduction to Programming by Christian Dimitrov (21-608-468). 

## Basic Description

This project fetches articles from The Guardian’s API, performs sentiment analysis, and visualizes the results over time. Users can provide a keyword and a year, and the application will:

1. Fetch articles from The Guardian’s API
2. Process and analyze the retrieved articles for sentiment (polarity and subjectivity).
3. Generate visualizations, including trends over time and sentiment distributions.
4. Display the analysis results in a web interface.

The project is hosted on render, aimed at being easily accessible for usage and can be accessed through the following link: https://guardiansentimentwebproject.onrender.com 

In case there are issues with the render, the project can also be run locally. For a more detailed explanation, please reference the relevant chapter below.

## Features

- Data Fetching: Retrieves up to 1000 articles from The Guardian API based on a provided keyword and year.
- Data Processing: Structures raw article data into a clean CSV file. 
- Sentiment Analysis: Applies text analysis to determine the polarity (positive/negative) and subjectivity (factual/opinion-based) of articles.
- Visualization: Generates static plots showing:
   1. Polarity over time
   2. Subjectivity over time
   3. Polarity distribution
   4. Subjectivity distribution
   5. Polarity vs. Subjectivity scatter plot
- Web Interface: A user-friendly Flask app to input parameters and view results.


## Project Structure

project/
   app.py                      # Flask application serving the web interface
   main.py                     # Main logic for fetching, analyzing, and visualizing articles
   data_processing.py          # Functions for processing and saving articles to CSV
   sentiment_analysis.py       # Functions for analyzing sentiment of articles
   visualization.py            # Functions for generating various plots
   guardian_api.py             # Functions for interacting with the Guardian API
   config.py                   # Configuration file with API keys and base URLs
   templates/
       index.html              # Landing page with input form for keyword/year
       results.html            # Results page displaying the generated charts
   static/
       images/                 # Directory where generated plots and CSV files are saved


## Requirements

- Python 3.8+ recommended.
- Virtual environment (optional but recommended).

### Python Dependencies (Necessary Packages)
- Flask (for the web server and handling requests)
- Requests (for fetching articles from The Guardian’s API)
- Pandas (for data processing and CSV handling)
- Matplotlib (for visualization)
- TextBlob (for sentiment analysis)

To install dependencies, run:

**pip install Flask gunicorn requests pandas matplotlib textblob**

Note: running requirements.txt struggles to build the wheel for some reason

## Configuration

Set your Guardian API key in config.py: (an active key is currently uploaded)

## Running the Application on Render
The github repository https://github.com/chrisf3/GuardianSentimentWebProject was integrated with Render, for active hosting and easy access to the project. The project web interface can hence be accessed through:

https://guardiansentimentwebproject.onrender.com/

Please note, sometimes the render application doesn't work. Therefor the optionality to run locally also exists.  

## Running the Application Locally
To run locally, please follow the following steps. The 

1. Clone the repository
2. Optional: Create and activate a virtual environment:
3. Install dependencies: "**Build Command**: pip install Flask gunicorn requests pandas matplotlib textblob"
4. Run app.py
5. Access the Web Interface - Open your browser and go to http://127.0.0.1:5000.
6. Run an Analysis:
   - Enter a keyword (e.g., "climate") and a year (e.g., "2020") on the index page.
   - Submit the form.
   - The application will fetch articles, run sentiment analysis, generate plots, and display them on the results page.

Note: Step 4 can also be achieved by running "gunicorn app:app" in the terminal

## Viewing Results

   - After processing, the generated CSV and images will be stored in static/images/.
   - The results page (/results) displays all the generated plots.
   - You can download the CSV directly from static/images/guardian_articles.csv if needed.

## Customization

   - Modify the max_articles or the moving_average_window in main.py to adjust data retrieval scales and smoothing.
   - Change visualization styles or add new charts by editing visualization.py.
   - Integrate additional NLP or sentiment models in sentiment_analysis.py as needed.


## Troubleshooting

   - No Articles Found: If you get a "No articles found" error, try a different keyword or ensure your API key is valid.
   - API Limits: The Guardian API may have rate limits. If you encounter issues, consider reducing max_articles or using caching.
   - Missing Plots: Ensure that static/images/ is writable and that all plotting libraries are installed.

## ChatGPT Disclaimer
ChatGPT was used in the process of developing the app. It was used to help develop a draft structure, enhance certain code structures, as well as for troubleshooting. The integration between the html and py code, in app.py was fully developed with the usage of ChatGPT. 

