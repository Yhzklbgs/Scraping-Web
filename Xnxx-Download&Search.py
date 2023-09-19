import requests
from bs4 import BeautifulSoup
import random

def xnxxsearch(query):
    base_url = 'https://www.xnxx.com'
    page_number = random.randint(1, 3)
    url = f'{base_url}/search/{query}/{page_number}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = []
        url = []
        desc = []
        results = []
        mozaiques = soup.find_all('div', class_='mozaique')
        for mozaique in mozaiques:
            thumbs = mozaique.find_all('div', class_='thumb')
            for thumb in thumbs:
                link = base_url + thumb.find('a').get('href').replace('/THUMBNUM/', '/')
                url.append(link)
        for mozaique in mozaiques:
            thumb_unders = mozaique.find_all('div', class_='thumb-under')
            for thumb_under in thumb_unders:
                description = thumb_under.find('p', class_='metadata').text
                desc.append(description)
                title_element = thumb_under.find('a')
                title_text = title_element.get('title')
                title.append(title_text)
        for i in range(len(title)):
            results.append({'title': title[i], 'info': desc[i], 'link': url[i]})
        return {'code': 200, 'status': True, 'result': results}
    except requests.exceptions.RequestException as err:
        return {'code': 503, 'status': False, 'result': str(err)}

def xnxxdl(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('meta', property='og:title')['content']
        duration = soup.find('meta', property='og:duration')['content']
        image = soup.find('meta', property='og:image')['content']
        video_type_tag = soup.find('meta', property='og:video:type')
        videoType = video_type_tag['content'] if video_type_tag else 'Unknown'
        video_width_tag = soup.find('meta', property='og:video:width')
        videoWidth = video_width_tag['content'] if video_width_tag else 'Unknown'
        video_height_tag = soup.find('meta', property='og:video:height')
        videoHeight = video_height_tag['content'] if video_height_tag else 'Unknown'
        info = soup.find('span', class_='metadata').text
        videoScript = soup.select_one('#video-player-bg > script:nth-child(6)').string
        files = {
            'low': videoScript.split('html5player.setVideoUrlLow(\'', 1)[-1].split('\');', 1)[0],
            'high': videoScript.split('html5player.setVideoUrlHigh(\'', 1)[-1].split('\');', 1)[0],
            'HLS': videoScript.split('html5player.setVideoHLS(\'', 1)[-1].split('\');', 1)[0],
            'thumb': videoScript.split('html5player.setThumbUrl(\'', 1)[-1].split('\');', 1)[0],
            'thumb69': videoScript.split('html5player.setThumbUrl169(\'', 1)[-1].split('\');', 1)[0],
            'thumbSlide': videoScript.split('html5player.setThumbSlide(\'', 1)[-1].split('\');', 1)[0],
            'thumbSlideBig': videoScript.split('html5player.setThumbSlideBig(\'', 1)[-1].split('\');', 1)[0]
        }
        result = {
            'title': title,
            'URL': url,
            'duration': duration,
            'image': image,
            'videoType': videoType,
            'videoWidth': videoWidth,
            'videoHeight': videoHeight,
            'info': info,
            'files': files
        }
        return {'status': 200, 'result': result}
    except requests.exceptions.RequestException as err:
        return {'code': 503, 'status': False, 'result': str(err)}

# Example usage:
search = xnxxsearch(input('Title ? : '))
print(search)
download = xnxxdl(input('Url Download ? : '))
print(download)
