import sys
import csv
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

# Open a new CSV file in write mode
with open('articles.csv', 'w', newline='', encoding='utf-8') as article:

    # Create a CSV writer object
    csvwriter = csv.writer(article)

    # Write the header row
    csvwriter.writerow(['Title', 'Author'])

    for title, author in zip(title_list, author_list):
        csvwriter.writerow([title, author])