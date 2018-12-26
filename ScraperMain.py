from bs4 import BeautifulSoup
import re
import requests

raw_Data = requests.get('https://umggaming.com/leaderboards')

soup = BeautifulSoup(raw_Data.text, 'html.parser')

data = []
table = soup.find('table', {'id': 'leaderboard-table'})
body = table.find('tbody')

for tr in body.find_all('tr'):
    place = tr.find_all('td')[0].text.strip()
    name = tr.find_all('td')[1].find_all('a')[1].text.strip()
    xp = tr.find_all('td')[3].text.strip()

    print(str(place), name, xp)

    # for td in tr.find_all('td'):
    #     print(td)
    #     values = [a.text for a in td.find_all('a')]
    #     data.append(values)

#print(data)
# with open('test.html', 'r') as html_doc:
#     html_contents = html_doc.read()
#
#     # phones = re.findall(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})', html_contents)
#     # emails = re.findall(r'[\d\w\.]+@', html_contents)
#     soup = BeautifulSoup(html_contents, 'html.parser')
#
#     data = []
#
#     div = soup.find('div', {'class': 'special_table'})
#
#     for tr in div.find_all('tr'):
#         values = [td.text for td in tr.find_all('td')]
#         data.append(values)
#
#     # for tr in soup.find_all('tr', {'class': 'special'}):
#     #     values = [td.text for td in tr.find_all('td')]
#     #     data.append(values)
#
#     print(data)


