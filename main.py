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


def make_book_list(data):
    books = []
    for item in data:
        book = {}
        book["title"] = item.get("title", "Unknown")
        book["year"] = item.get("first_publish_year", "Unknown")
        book["pages"] = item.get("number_of_pages_median", "Unknown")
        books.append(book)
    return books


def show_books(books):
    if len(books) == 0:
        print("No books were found.")
        return
    for i in range(len(books)):
        if i == 10:
            break
