import requests, random
from bs4 import BeautifulSoup

def xvideosdl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('meta', {'property': 'og:title'})['content']
        keyword = soup.find('meta', {'name': 'keywords'})['content']
        views = soup.select_one('div#video-tabs > div > div > div > div > strong.mobile-hide').text + " views"
        vote = soup.select_one('div.rate-infos > span.rating-total-txt').text
        likes = soup.select_one('span.rating-good-nbr').text
        dislikes = soup.select_one('span.rating-bad-nbr').text
        thumb = soup.find('meta', {'property': 'og:image'})['content']
        video_url = soup.select_one('#html5video > #html5video_base > div > a')['href']
        result = {
            'status': 200,
            'result': {
                'title': title,
                'url': video_url,
                'keyword': keyword,
                'views': views,
                'vote': vote,
                'likes': likes,
                'dislikes': dislikes,
                'thumb': thumb
            }
        }
        return result
    except requests.exceptions.RequestException as err:
        return {'status': 500, 'error': str(err)}

def xvideos_search(query):
    try:
        random_page = str(random.randint(1, 10))
        url = f'https://www.xvideos.com/?k={query}&p={random_page}'
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = []
        duration = []
        quality = []
        url = []
        thumb = []
        result = []
        for item in soup.select('div.mozaique > div > div.thumb-under > p.title'):
            title.append(item.find('a')['title'])
            duration.append(item.select_one('span.duration').text)
            quality_elem = item.select_one('span.video-hd-mark')
            quality_text = quality_elem.text if quality_elem else "Unknown"
            quality.append(quality_text)
            url.append('https://www.xvideos.com' + item.find('a')['href'])
        for item in soup.select('div.mozaique > div > div > div.thumb > a'):
            thumb.append(item.find('img')['data-src'])
        for i in range(len(title)):
            result.append({
                'title': title[i],
                'duration': duration[i],
                'quality': quality[i],
                'thumb': thumb[i],
                'url': url[i]
            })
        return result
    except requests.exceptions.RequestException as err:
        return {'status': 500, 'error': str(err)}

# Usage examples:
search = xvideos_search(input('Title ? : '))
print(search)
download = xvideosdl(input('Url Download ? : '))
print(download)
