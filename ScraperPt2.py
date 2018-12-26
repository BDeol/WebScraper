from bs4 import BeautifulSoup
import requests
import csv
import unicodedata

html_Source = requests.get('http://coreyms.com')
soup = BeautifulSoup(html_Source.text, 'html.parser')

articles = soup.find_all('article')

with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Title", "Description", "Youtube Link"])
    for article in articles:
        title = article.header.h2.a.text
        summary = article.div.p.text
        try:
            youtube_fulllink = article.div.iframe['src']
            youtube_code = youtube_fulllink.split('/')[4].split('?')[0]
            youtube_parsedlink = 'https://youtube.com/watch?v={}'.format(youtube_code)
        except Exception as e:
            youtube_parsedlink = None
        writer.writerow([unicodedata.normalize('NFKD', title).encode('ascii', 'ignore'),
                         unicodedata.normalize('NFKD', summary).encode('ascii', 'ignore'), youtube_parsedlink])



