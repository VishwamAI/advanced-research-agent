import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time

class ResearchAgent:
    def __init__(self):
        self.data = []
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def fetch_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching {url}: {e}")
            return None

    def parse_page(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        # Example: Extracting all paragraph texts
        paragraphs = soup.find_all('p')
        for p in paragraphs:
            self.data.append(p.get_text())

    def save_data(self, filename):
        df = pd.DataFrame(self.data, columns=['Content'])
        df.to_csv(filename, index=False)

    def run(self, url, output_file):
        html_content = self.fetch_page(url)
        if html_content:
            self.parse_page(html_content)
            self.save_data(output_file)
        else:
            logging.error("Failed to retrieve the page.")

    def run_with_rate_limiting(self, urls, output_file, delay=1):
        for url in urls:
            self.run(url, output_file)
            time.sleep(delay)

if __name__ == "__main__":
    agent = ResearchAgent()
    test_urls = ["https://example.com", "https://example.org"]
    output_file = "output.csv"
    agent.run_with_rate_limiting(test_urls, output_file, delay=2)
