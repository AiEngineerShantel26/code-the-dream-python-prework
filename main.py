import requests

url = "https://openlibrary.org/search.json"


def get_books(author):
    response = requests.get(url, params={"author": author})
    return response.json().get("docs", [])
