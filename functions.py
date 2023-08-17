import g4f
import requests
from bs4 import BeautifulSoup
import time
import feedparser
def ask(message):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{"role": "user", "content": message}])
def beautiful_soup_scrape(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"}
    response = requests.get(url,headers=headers)
    return BeautifulSoup(response.content, "html.parser")
def rss_scrape(url):
    f = feedparser.parse(url)
    results = [entry for entry in f.entries if time.time() - time.mktime(entry.published_parsed) < (86400)]
    dict = {}
    for result in results:
        dict[result.title] = result.link
    return dict