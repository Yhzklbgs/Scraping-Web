import random
import requests
from bs4 import BeautifulSoup

def quotes_anime():
    page = random.randint(1, 184)
    url = f'https://otakotaku.com/quote/feed/{page}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.text
        soup = BeautifulSoup(data, 'html.parser')
        hasil = []
        quotes_list = soup.find_all('div', class_='kotodama-list')
        for h in quotes_list:
            link = h.find('a')['href']
            gambar = h.find('img')['data-src']
            karakter = h.find('div', class_='char-name').text.strip()
            anime = h.find('div', class_='anime-title').text.strip()
            episode = h.find('div', class_='meta').text.strip()
            up_at = h.find('small', class_='meta').text.strip()
            quotes = h.find('div', class_='quote').text.strip()
            hasil.append({
                'link': link,
                'gambar': gambar,
                'karakter': karakter,
                'anime': anime,
                'episode': episode,
                'up_at': up_at,
                'quotes': quotes
            })
        return hasil
    except Exception as e:
        return str(e)

# Example usage:
quotes = quotes_anime()
print(quotes)
