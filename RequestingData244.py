import requests
# from bs4 import BeautifulSoup

# Open Website Look at the inspect elements (Name : status)
# Example <Response [200]> - Matches with the website status

res = requests.get('https://news.ycombinator.com/news')
print(res.text)
