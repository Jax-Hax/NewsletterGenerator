from functions import *
from readEmail1 import *
# Newsletters
# sign in with gmail

# fetch todays emails

# check the email and run different things depending on it, so for TLDR say remove sponsors, summarize everything, include the link (with normal code do this yourself)
# AI Papers
# https://ai.papers.bar/papers/recent/
emails = getEmails()
for email in emails:
    prompt = f"give me the most important points from this email, key insights and quotes. Do not introduce yourself or do anything else, only write: Key insights: and key quotes:. Here is the email: {email}"
    response = ask(prompt)
    print(response)
# Articles
# techcrunch
#techxplore = rss_scrape("https://techxplore.com/rss-feed/machine-learning-ai-news/")
#bensbites = rss_scrape("https://rss.beehiiv.com/feeds/moS8GVKETl.xml?utm_source=bensbites&utm_medium=newsletter")
#techcrunch = rss_scrape("https://techcrunch.com/category/artificial-intelligence/feed")
#print(techcrunch)
# maybe ai youtube channels latest videos
#print(ask(f"write a one sentence summary of each of these articles: {techcrunch}"))


# collect all news sources

# run all the titles through chatgpt saying return a list of the titles of the articles that look to be covering the same topic, being comma seperated no spaces and no newlines. Only use one, keep the other, just so there aren't duplicates of the same article.