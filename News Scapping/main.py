from bs4 import BeautifulSoup
import requests


def news_scrape():
    url = requests.get('http://www.inshorts.com/en/read/technology').text
    soup = BeautifulSoup(url,'lxml')
    newses=soup.find_all('div', class_='news-card z-depth-1')
    only=soup.find('div',class_='news-card-author-time news-card-author-time-in-content')
    for index,news in enumerate(newses):
        hl=news.find('a', class_='clickable').text
        time=news.find('span',class_='time').text
        date=news.find('span',class_='date').text
        summary=news.find('div', class_='news-card-content news-right-box').text
        more_info=only.a['href']
        
        with open(f'News/{index}.txt','w') as f:
            
            f.write(f'{time.strip()} on {date.strip()},\n')
            f.write(f'Headline: {hl.strip()}\n')
            f.write(f'Summary: {summary.strip()}\n')
            f.write(f'More Info: {more_info.strip()}\n')
        print(f'File saved: {index}')
