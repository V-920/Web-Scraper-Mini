import requests
from bs4 import BeautifulSoup
url = input("Enter Url: ")
url = 'https://www.' + url
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title
content = soup.get_text()
print(title)
print(content)