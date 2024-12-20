#app.py - main project file
#this python code was mostly generated with ChatGPT, to help create the intersection between the front-end html code and the backend application

from flask import Flask, render_template, request, redirect, url_for
from main import process_keyword_year  # Import the function from main.py for processing the input
import os

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the homepage (index)
@app.route("/")
def index():
    """
    Render the index page where users can input the keyword and year.
    """
    return render_template("index.html")

# Define the route for processing the user input
@app.route("/process", methods=["POST"])
def process():
    """
    Handle form submission:
    - Extract the keyword and year from the POST request.
    - Call the processing function to fetch and analyze data.
    - Redirect to the results page upon successful processing.
    """
    # Get input data from the form
    keyword = request.form.get("keyword")
    year = request.form.get("year")

    # Validate the input
    if not keyword or not year:
        return "Please provide both a keyword and a year."

    # Call the main processing function
    try:
        process_keyword_year(keyword, year)  # Perform data processing (e.g., fetch articles, generate visualizations)
    except ValueError as e:
        # Handle specific errors (e.g., no data found for the keyword)
        return str(e)
    except Exception as e:
        # General error handling for unexpected issues
        return f"An error occurred: {e}"

    # Redirect to the results page with the keyword and year as query parameters
    return redirect(url_for("results", keyword=keyword, year=year))

# Define the route for displaying the results page
@app.route("/results")
def results():
    """
    Render the results page:
    - Retrieve the keyword and year from the query parameters.
    - Pass the keyword and year to the template for dynamic content.
    """
    # Retrieve query parameters for the keyword and year
    keyword = request.args.get("keyword", "Unknown Topic")
    year = request.args.get("year", "Unknown Year")

    # Render the results page with the provided keyword and year
    return render_template("results.html", keyword=keyword, year=year)

# Run the application
if __name__ == "__main__":
    """
    Ensure the required directories exist and start the Flask development server.
    """
    # Create the static/images directory if it doesn't already exist
    os.makedirs("static/images", exist_ok=True)

    # Start the Flask application in debug mode for easier development and troubleshooting
    app.run(debug=True)