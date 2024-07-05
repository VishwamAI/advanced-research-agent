# Research Agent

## Overview
The Research Agent is a Python script designed to collect data from the internet by scraping web pages. It fetches, parses, and saves the content of web pages into a CSV file. The script includes features such as error handling, logging, and rate limiting to ensure robust and efficient data collection.

## Features
- Fetches web page content using HTTP GET requests.
- Parses HTML content to extract text from paragraph elements.
- Saves the extracted data into a CSV file.
- Includes error handling for network and parsing errors.
- Logs the script's execution for monitoring and debugging.
- Implements rate limiting to avoid overloading servers when scraping multiple pages.

## Requirements
- Python 3.10.12
- Requests library
- Beautiful Soup library
- Pandas library

## Installation
Ensure that Python 3.10.12 and pip are installed on your system. Then, install the required libraries using pip:
```bash
pip3 install requests beautifulsoup4 pandas
```

## Usage
To use the Research Agent, run the `research_agent.py` script with the desired URLs and output file. The script can be customized to extract different types of data based on specific requirements.

### Example
```python
if __name__ == "__main__":
    agent = ResearchAgent()
    test_urls = ["https://example.com", "https://example.org"]
    output_file = "output.csv"
    agent.run_with_rate_limiting(test_urls, output_file, delay=2)
```

### Running the Script
Execute the script using Python:
```bash
python3 research_agent.py
```

## Customization
The `parse_page` method can be customized to extract different types of data from web pages. Modify the method to suit your specific data collection needs.

### Example Customization
```python
def parse_page(self, html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Example: Extracting all paragraph texts
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        self.data.append(p.get_text())
```

## Logging
The script uses Python's built-in logging module to log information about its execution. Logs include details about successful and failed requests, as well as any errors encountered during the scraping process.

## Rate Limiting
The `run_with_rate_limiting` method introduces a delay between consecutive requests to avoid overloading servers. The delay can be adjusted by modifying the `delay` parameter.

### Example
```python
agent.run_with_rate_limiting(test_urls, output_file, delay=2)
```

## Conclusion
The Research Agent is a versatile and robust tool for collecting data from the internet. By customizing the parsing logic and adjusting the rate limiting, it can be adapted to various data collection needs. For any questions or further customization, please refer to the script's documentation and comments.
