class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: {a}\nAuthor: {b}\nPages: {c}".format(a = self.title, b = self.author, c = self.pages)

    def __len__(self):
        return self.pages

b = Book("Python", "Isaac", 200)
print(b)
print(len(b))
