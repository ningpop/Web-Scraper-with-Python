import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

# print(indeed_soup)

pagination = indeed_soup.find("div", {"class":"pagination"})

# print(pagination)

pages = pagination.find_all('a')

spans = []

for page in pages:
    # print(page.find("span"))
    spans.append(page.find("span"))

print(spans[:-1])