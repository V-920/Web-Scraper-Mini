import requests
from bs4 import BeautifulSoup
import csv
import re
url = input("Enter Url: ")
url = 'https://www.' + url
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.title.get_text(strip=True) #the strip removes the HTML tags
for element in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
    element.decompose()
content = soup.get_text(separator=" ", strip=True)
content = re.sub(r'\s+', ' ', content)  # Replace multiple whitespace with a single space
print(title)
print(content)
with open('Scraped.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0: 
        writer.writerow(['Title', 'Content'])
    writer.writerow([title, content])