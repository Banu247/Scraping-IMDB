# IMDb Website Scraping with BeautifulSoup and Selenium

This project showcases how to scrape data from the IMDb website using Python libraries BeautifulSoup and Selenium. BeautifulSoup is utilized for parsing HTML content, while Selenium is employed to automate web browsing, facilitating interaction with dynamic content.

## Prerequisites
- Python 3.x installed
- Libraries: BeautifulSoup, Selenium, pandas

## Installation
1. Install required Python libraries using pip:
2. Download and install the appropriate WebDriver for your browser (e.g., ChromeDriver for Google Chrome).

## Usage
1. Run the `imdb_scraping.py` script.
2. The script will open a web browser, navigate to the IMDb website, and scrape the desired data.
3. The scraped data will be stored in a CSV file named `imdb_movies.csv`.

## Description
- The `imdb_scraping.py` script uses Selenium to automate web browsing and BeautifulSoup to parse HTML content.
- It navigates to the IMDb website, selects the desired categories or search criteria, and extracts relevant movie data such as title, rating, and year of release.
- The extracted data is then stored in a pandas DataFrame and exported to a CSV file (`imdb_movies.csv`) for further analysis or processing.

## Files
- `imdb_scraping.py`: Python script for scraping the IMDb website.
- `imdb_movies.csv`: CSV file containing scraped movie data.

## Acknowledgments
- This project is for educational purposes and demonstrates web scraping techniques using Python.
- Please ensure compliance with IMDb website terms of service while scraping data.

