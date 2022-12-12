class Book:
    title = None
    author = None
    year = 0
    rating = 0

    def __init__(self, t, a, y, r):
        self.title = t
        self.author = a
        self.year = y
        self.rating = r

    def __str__(self):
        return f"{self.title} ({self.year} by {self.author} -- Rating = {self.rating}"

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_year(self):
        return self.year
    def get_rating(self):
        return self.rating
