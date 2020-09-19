import requests
from bs4 import BeautifulSoup

indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, 'html.parser')

# print(indeed_soup)

pagination = indeed_soup.find("div", {"class":"pagination"})

# print(pagination)

links = pagination.find_all('a')

pages = []

for link in links[:-1]:
    # print(page.find("span"))
    # pages.append(link.find("span").string)
    pages.append(int(link.string))

max_page = pages[-1]

print(max_page)