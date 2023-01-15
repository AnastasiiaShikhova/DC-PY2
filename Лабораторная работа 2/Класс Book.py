BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

class Book:
    def __init__(self, id_: int, name: str, pages: int):
        if not isinstance(id_, (int)):
            raise TypeError("Индентификатор книги - целое число")
        if id_ < 0:
            raise ValueError("Идентификатор книги - не отрицательное число")
        self.id = id_

        self.name = name

        if not isinstance(pages, (int)):
            raise TypeError("В книге целое число страниц")
        if pages <= 0:
            raise ValueError("В книге не может быть меньше одной страницы")
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"



if __name__ == '__main__':

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)

    print(list_books)
