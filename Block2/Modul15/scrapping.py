import requests
import re
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from time import sleep


url = 'https://www.ukr.net/news/technologies.html'

def handle_met(url):

    htm = requests.get(url)
    html = htm.text[:100]
    #soup = BeautifulSoup(html, 'lxml')
    #print(soup)
    minimum = html.find('class_="im-tl_a"')
    print(html)
    #inform = soup.find_all('div', class_='im-pr')[:9]
    #time = soup.find_all('time', class_='im-tm')[:9]
    #for i in range(0,9):
     #   print(f'{time[i].text} -- {minimum[i].text}--{inform[i].text}')
    #for tim in time:
        #print(tim.text)
    #for inf in inform:
       # print(inf.text)
   # for min in minimum:
        #print(min.text)
          #  max = soup.find('span', class_='wwt_tmp wwt_max')
          #  maxs = max.text
          #  min = minimum.text
         #   s = ''.join(maxs.split())
          #  m = ''.join(min.split())

    
       

if __name__ == "__main__":
    handle_met(url)
    
   