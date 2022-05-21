import requests


def shorten(token, url):
    bitly_url = "https://api-ssl.bitly.com/v4/shorten"
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.post(bitly_url, headers=headers, json={"long_url": url})
    response.raise_for_status()
    return response.json()
