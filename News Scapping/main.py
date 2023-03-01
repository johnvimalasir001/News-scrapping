from bs4 import BeautifulSoup
import requests

details = []
def news_scrape():
    url = requests.get('http://www.inshorts.com/en/read/technology').text
    soup = BeautifulSoup(url,'lxml')
    newses=soup.find_all('div', class_='news-card z-depth-1')
    for news in newses:
        hl=news.find('a', class_='clickable').text
        summary = news.find(class_='news-card-content').find('div').text
        
        detail=(f"Headline:{hl.strip()}\nSummary:{summary.strip()}").split("\n")
        details.append(detail)
    return details

print(news_scrape())
