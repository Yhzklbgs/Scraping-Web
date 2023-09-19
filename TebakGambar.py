import requests
from bs4 import BeautifulSoup
import random

def tebakgambar():
    result = []

    try:
        url = 'https://jawabantebakgambar.net/all-answers/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the total number of images available (2836 in this case)
        total_images = 2836

        # Generate a random number between 2 and total_images
        random_index = random.randint(2, total_images)

        # Get the image and answer for the random index
        image_element = soup.select_one(f'#images > li:nth-child({random_index}) > a img')
        answer_element = soup.select_one(f'#images > li:nth-child({random_index}) > a img[alt]')

        if image_element and answer_element:
            image_url = 'https://jawabantebakgambar.net' + image_element['data-src']
            answer = answer_element['alt']

            result.append({
                'image': image_url,
                'answer': answer
            })
    except Exception as e:
        return str(e)

    return result

# Example usage:
tebakgambar_result = tebakgambar()
if tebakgambar_result:
    for item in tebakgambar_result:
        print(item)
else:
    print('Failed to retrieve Tebak Gambar data.')
