from bs4 import BeautifulSoup
import requests

details = []
def news_scrape():
    url = requests.get('http://www.inshorts.com/en/read/technology').text
    soup = BeautifulSoup(url,'lxml')
    newses=soup.find_all('div', class_='news-card z-depth-1')
    only=soup.find('div',class_='news-card-author-time news-card-author-time-in-content')
    for index,news in enumerate(newses):
        hl=news.find('a', class_='clickable').text
        time=news.find('span',class_='time').text
        date=news.find('span',class_='date').text
        summary = news.find(class_='news-card-content').find('div').text
        more_info=only.a['href']
        
        detail=(f"Headline:{hl.strip()}\nSummary:{summary.strip()}\nMore:{more_info.strip()}").split("\n")
        details.append(detail)
    return details

print(news_scrape())
