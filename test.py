import time
import feedparser
def scrape_articles():
    url = "https://rss.beehiiv.com/feeds/moS8GVKETl.xml?utm_source=bensbites&utm_medium=newsletter"
    f = feedparser.parse(url)
    results = [entry for entry in f.entries if time.time() - time.mktime(entry.published_parsed) < (86400)]
    dict = {}
    print(results[0].content)
    for result in results:
        dict[result.content] = result.link
    print(dict)
scrape_articles()