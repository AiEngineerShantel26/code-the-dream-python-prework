import requests

url = "https://openlibrary.org/search.json"


def get_books(author):
    try:
        response = requests.get(url, params={"author": author})
        response.raise_for_status()
        data = response.json()
        return data.get("docs", [])
    except requests.exceptions.RequestException:
        print("There was a problem connecting to Open Library.")
        return []
