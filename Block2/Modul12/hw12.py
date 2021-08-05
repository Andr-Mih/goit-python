import requests
import re
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from time import sleep


urls = ['https://meteo.ua/172/zaporoje', 'https://sinoptik.ua/погода-запорожье']

async def handle_met(url):

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:

            html = await resp.text()
            soup = BeautifulSoup(html, 'lxml')
            minimum = soup.find('span', class_='wwt_tmp wwt_min')
            max = soup.find('span', class_='wwt_tmp wwt_max')
            maxs = max.text
            min = minimum.text
            s = ''.join(maxs.split())
            m = ''.join(min.split())

    
    print(f'Погода в Запорожье на meteo.ua     {s} || {m}')
            
    
async def handle_sin(url):

    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:

            html = await resp.text()
            
            soup = BeautifulSoup(html, 'lxml')
            minimum = soup.find('div', class_='min')
            max = soup.find('div', class_='max')
            maxs = max.text
            min = minimum.text
            s = ''.join(maxs.split())
            m = ''.join(min.split())

            
        print(f'Погода в Запорожье на Sinoptik.ua  {s} || {m}')
            

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
   
    features = []
    for i in urls:
        if i.find('sinoptik'):
            features.append(loop.create_task(handle_sin(i)))
        if i.find('meteo'):
            features.append(loop.create_task(handle_met(i)))
    wait_task = asyncio.wait(features)
    loop.run_until_complete(wait_task)
    
   