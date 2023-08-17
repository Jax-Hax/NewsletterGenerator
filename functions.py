import g4f
from bs4 import BeautifulSoup
def ask(message):
    return g4f.ChatCompletion.create(model=g4f.models.gpt_4, messages=[{"role": "user", "content": message}])
