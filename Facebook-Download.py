import requests
from bs4 import BeautifulSoup

def fbdown(link):
    url = 'https://www.getfvid.com/downloader'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Cookie': '_ga=GA1.2.1310699039.1624884412; _pbjs_userid_consent_data=3524755945110770; cto_bidid=rQH5Tl9NNm5IWFZsem00SVVuZGpEd21sWnp0WmhUeTZpRXdkWlRUOSUyQkYlMkJQQnJRSHVPZ3Fhb1R2UUFiTWJuTVRUa1hYVzZMcElQaFZjSHFBNVdMeGw2Yk1MMFQwV3FHR3pKckMxSGh2WUlYRjBZRjFtWjNLbXJZU0V3UGc1Q3NlWmxCTjlzQ0RQQmVoMHBwZGpRckJzUkJKJTNE; cto_bundle=g1Ka319NaThuSmh6UklyWm5vV2pkb3NYaUZMeWlHVUtDbVBmeldhNm5qVGVwWnJzSUElMkJXVDdORmU5VElvV2pXUTJhQ3owVWI5enE1WjJ4ZHR5NDZqd1hCZnVHVGZmOEd0eURzcSUyQkNDcHZsR0xJcTZaRFZEMDkzUk1xSmhYMlY0TTdUY0hpZm9NTk5GYXVxWjBJZTR0dE9rQmZ3JTNEJTNE; _gid=GA1.2.908874955.1625126838; __gads=ID=5be9d413ff899546-22e04a9e18ca0046:T=1625126836:RT=1625126836:S=ALNI_Ma0axY94aSdwMIg95hxZVZ-JGNT2w; cookieconsent_status=dismiss',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'url': link
    }
    try:
        response = requests.post(url, headers=headers, data=data)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        result = {
            'Normal_video': soup.select_one('div.col-md-4.btns-download > p:nth-child(2) > a')['href'],
            'HD': soup.select_one('div.col-md-4.btns-download > p:nth-child(1) > a')['href'],
            'audio': soup.select_one('div.col-md-4.btns-download > p:nth-child(3) > a')['href']
        }
        return result
    except Exception as e:
        return str(e)

# Example usage
link = 'https://www.facebook.com/watch?v=793021315947431'  # Replace with the actual link
video_info = fbdown(link)
print('Normal Video:', video_info['Normal_video'])
print('HD Video:', video_info['HD'])
print('Audio:', video_info['audio'])
