import requests
from bs4 import BeautifulSoup

def simple_web_scraper(url):
    # Make a GET request to the website
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract information from the HTML
        # Modify this part based on the structure of the website you are scraping
        # Here, we are extracting all text within paragraph (p) tags
        paragraphs = soup.find_all('p')

        # Display the extracted information
        for paragraph in paragraphs:
            print(paragraph.get_text())

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

# Replace 'your_url_here' with the URL of the website you want to scrape
url_to_scrape = 'https://www.webscraper.io/test-sites/e-commerce/allinone'
simple_web_scraper(url_to_scrape)
