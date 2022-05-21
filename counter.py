import requests

BITLY_SHORTEN_API_URL = "https://api-ssl.bitly.com/v4/shorten"

BITLY_TOKEN = 'ab0c2990687fcacff260f38a9b98e9a9d847709d'


def shorten_link(token, url):
    response = requests.post(
        BITLY_SHORTEN_API_URL,
        headers={'Authorization': f'Bearer {token}'},
        json={"long_url": url}
    )

    response.raise_for_status()
    return response.json()


def main():
    url = input()
    print(shorten_link(BITLY_TOKEN, url)['link'])


if __name__ == '__main__':
    main()