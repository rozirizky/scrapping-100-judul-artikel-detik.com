import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

class Scrapping:
    def __init__(self, baseurl):
        self.baseurl = baseurl
        self.soup = None
        self.data = []
      

    def fetch_data(self,url):
        headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.content, 'html.parser')
        else:
            print("Error fetching data:", response.status_code)

    def article_link(self): 
        artikel = self.soup.find_all('article','list-content__item')
        links = []
        for a in range(0,len(artikel)):
            link = artikel[a].find('h3')
            judul = re.sub('\n','',link.text)
            links.append(judul)
        return links
    

if __name__ == "__main__":
    scraper = Scrapping("https://news.detik.com/indeks")
    judul = []
    for p in range(1,6):
        url = f"{scraper.baseurl}/{p}"
        scraper.fetch_data(url)
        products = scraper.article_link()
        judul.extend(products)
    data = {"Judul Berita": judul}

    df = pd.DataFrame(data)
    df.to_csv('detik.csv')