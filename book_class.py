class Book:
    def __init__(self, title, author, bookno, genre):
        self.title = title
        self.author = author
        self.bookno = bookno
        self.genre = genre
        print("Welcome to the Library Book Information System")
    def display_details(self):
        print("\n--- Book Details ---")
        print("Title       :", self.title)
        print("Author      :", self.author)
        print("Book Number :", self.bookno)
        print("Genre       :", self.genre)
b = Book("The Great Gatsby", "F. Scott Fitzgerald", "2A101", "Classic Literature")
b.display_details()
