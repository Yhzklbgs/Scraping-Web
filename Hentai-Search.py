from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup

def get_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random

def search_hentai(search):
    url = f"https://hentai.tv/?s={search}"
    headers = {
        'User-Agent': get_random_user_agent()
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        result = {
            'result': []
        }
        for div in soup.select('div.flex > div.crsl-slde'):
            thumbnail = div.find('img')['src']
            title = div.find('a').get_text().strip()
            views = div.find('p').get_text().strip()
            url = div.find('a')['href']
            result['result'].append({'thumbnail': thumbnail, 'title': title, 'views': views, 'url': url})
        return result

    except requests.exceptions.RequestException as err:
        print(err)
# Usage
search_query = input('WHICH TYPE HENTAI U WANT TO SEARCH ?\n')
result = search_hentai(search_query)
print(result)
