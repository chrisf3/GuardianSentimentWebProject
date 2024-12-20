#guardian.py

import requests
from config import CONFIG  # Import configuration constants, including API key and base URL


def fetch_articles(section=None, keyword=None, max_articles=1000, year=None):
    """
    Fetch articles from The Guardian API based on the provided filters.

    Parameters:
    - section (str, optional): Filter articles by section (e.g., "world", "sports").
    - keyword (str, optional): Search articles by a keyword (e.g., "climate change").
    - max_articles (int): Maximum number of articles to fetch.
    - year (int, optional): Year for filtering articles by date range.

    Returns:
    - List of articles (up to max_articles) containing metadata like title, URL, and publication date.
    """
    # Construct the API endpoint URL
    url = f"{CONFIG['GUARDIAN_BASE_URL']}/search"

    # Define API query parameters
    params = {
        **CONFIG["DEFAULT_PARAMS"],  # Load default parameters from the configuration
        "api-key": CONFIG["GUARDIAN_API_KEY"],  # Include the API key
        "page-size": 50,  # Number of results per API page
        "order-by": "relevance",  # Sort results by relevance
    }

    # Define date range for the query (if year is provided)
    from_date = f"{year}-01-01"
    to_date = f"{year}-06-30"

    # Add additional filters to the API parameters
    if section:
        params["section"] = section.lower()  # Convert section to lowercase
    if keyword:
        params["q"] = keyword  # Add keyword search filter
    if from_date:
        params["from-date"] = from_date  # Set the starting date for the query
    if to_date:
        params["to-date"] = to_date  # Set the ending date for the query

    articles = []  # List to store the fetched articles
    page = 1  # Initialize page counter

    # Fetch articles in a paginated manner until max_articles or no more results
    while len(articles) < max_articles:
        params["page"] = page  # Update the page number in the query
        response = requests.get(url, params=params)  # Make the API request

        # Handle errors if the request fails
        if response.status_code != 200:
            raise Exception(f"Failed to fetch articles: {response.status_code} - {response.text}")

        # Parse the JSON response
        data = response.json()
        results = data.get("response", {}).get("results", [])  # Extract articles
        total_pages = data.get("response", {}).get("pages", 0)  # Get the total number of pages

        # Stop fetching if there are no more results
        if not results:
            break

        # Add the fetched articles to the list
        articles.extend(results)

        # Stop if the desired number of articles or pages is reached
        if len(articles) >= max_articles or page >= total_pages:
            break

        page += 1  # Increment the page counter

    # Return the fetched articles, limited to max_articles
    return articles[:max_articles]
