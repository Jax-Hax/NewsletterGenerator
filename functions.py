import g4f
import requests
from bs4 import BeautifulSoup
def ask(message):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{"role": "user", "content": message}])
def scrape_site(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.get(url,headers=headers)
    return BeautifulSoup(response.content, "html.parser")
def scrape_techxplore():
    """Scrape TechXplore for machine learning and AI articles published today."""
    url = "https://techxplore.com/machine-learning-ai-news/sort/date/1d/"
    soup = scrape_site(url)
    articles = soup.find_all("article")
    dict = {}
    for article in articles:
        title = article.find("h2").text
        link = article.find("a")["href"]
        dict[title] = link
    return dict
