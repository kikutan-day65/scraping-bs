import sys
import requests
from bs4 import BeautifulSoup


# Set default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.mlbtraderumors.com/cleveland-guardians/'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')

main_content = soup.find('main')

titles = main_content.find_all('h2', class_='entry-title')

for title in titles:
    print(title.text)