import requests
from bs4 import BeautifulSoup
import csv
import re
import os
import time
url = input("Enter Url: https://www.")
url = 'https://www.' + url
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title.get_text(strip=True)
for element in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
    element.decompose()
content = soup.get_text(separator=" ", strip=True)
content = re.sub(r'\s+', ' ', content)
print(content)
with open('Scraped.csv', 'a', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    if file.tell() == 0: 
        writer.writerow(['Title', 'Content'])
    writer.writerow([title, content])
script_dir = os.path.dirname(os.path.abspath(__file__))
full_path = os.path.join(script_dir, 'Scraped.csv')
time.sleep(1)
os.startfile(full_path)
time.sleep(10)
