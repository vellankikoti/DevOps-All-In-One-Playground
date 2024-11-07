import requests
from bs4 import BeautifulSoup

def scrape_titles(urls):
    titles = {}
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles[url] = soup.title.string if soup.title else 'No Title'
    return titles

print(scrape_titles(['https://example.com', 'https://openai.com']))
