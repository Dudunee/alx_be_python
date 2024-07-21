class Book:
    def __init__(self, title, author, year: int):
        self.title = title
        self.author = author
        self.year = year
    def __del__(self):
        print(f"deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        return f"book('{self.title}', '{self.author}', {self.year})"
    
