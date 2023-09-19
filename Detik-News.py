import requests
from bs4 import BeautifulSoup

def detik_news(query):
    url = f'https://www.detik.com/search/searchall?query={query}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if request fails
        soup = BeautifulSoup(response.text, 'html.parser')
        hasil = []
        articles = soup.find_all('article')
        for article in articles:
            title = article.find('img')['title']
            link = article.find('a')['href']
            img = article.find('img')['src']
            
            iwak = {
                'Title': title,
                'Link': link,
                'Image': img
            }
            
            hasil.append(iwak)
        return hasil
    except Exception as e:
        return {'error': str(e)}

# Example usage:
query = 'pertalite'
result = detik_news(query)
print(result)
