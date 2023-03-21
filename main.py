import sys
import requests
from bs4 import BeautifulSoup


# Set default encoding to utf-8
sys.stdout.reconfigure(encoding='utf-8')

url = 'https://www.mlbtraderumors.com/cleveland-guardians?show=all'
page = requests.get(url)

soup = BeautifulSoup(page.content, 'lxml')

main_content = soup.find('main')
titles = main_content.find_all('h2', class_='entry-title')
authors = main_content.find_all('span', class_='entry-author-name')

title_list = [title.text for title in titles[:10]]
author_list = [author.text for author in authors[:10]]

for article in zip(title_list, author_list):
    print(article)