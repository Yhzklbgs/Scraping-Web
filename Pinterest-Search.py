import requests
import random

def pinterest(query):
    try:
        url = f"https://www.pinterest.com/resource/BaseSearchResource/get/?source_url=%2Fsearch%2Fpins%2F%3Fq%3D{query}&data=%7B%22options%22%3A%7B%22isPrefetch%22%3Afalse%2C%22query%22%3A%22{query}%22%2C%22scope%22%3A%22pins%22%2C%22no_fetch_context_on_resource%22%3Afalse%7D%2C%22context%22%3A%7B%7D%7D&_={random.randint(1, 999999999999)}"
        response = requests.get(url)
        data = response.json()
        if "resource_response" in data and "data" in data["resource_response"] and "results" in data["resource_response"]["data"]:
            results = data["resource_response"]["data"]["results"]
            
            if results:
                random_result = random.choice(results)
                return {
                    "status": 200,
                    "url": random_result["images"]["orig"]["url"]
                }
        return {
            "status": 404,
            "message": "No results found"
        }
    except Exception as e:
        return {
            "status": 500,
            "message": str(e)
        }

# Example usage
result = pinterest("cat")
print(result)
