def classify_length(page_count):  # page_count = classifer parameter
    if page_count >= 200:
        return "Long"
    else:
        return "Short"


def display_book(title, label):  # title = future string, label = label stores the value
    print(f"{title} - {label}")


def process_books(books):  # parameter = books (returns the whole list)
    for book in books:
        page_count = book["pages"]  # page_count contains only the integer
        label = classify_length(page_count)
        title = book["title"]

        display_book(title, label)


def main():
    books = [
        {"title": "Moon Base", "pages": 120},  # pages = dictionary key
        {"title": "Deep River", "pages": 310},
        {"title": "Moon Base", "pages": 80},
    ]

    process_books(books)


if __name__ == "__main__":
    main()
