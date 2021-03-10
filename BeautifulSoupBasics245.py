import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')

# print(soup.find(id='score_25303532'))
# print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a')) - all links
# print(soup.a) - find 1 a tag




