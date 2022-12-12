import csv
from book import Book

book_list = []


def parser(cs):  # this function parses the CSV and writes data to the list
    all_books = open(cs, "r+")
    for book in all_books:
        split = book.split(",")
        messy_rating = split[3]
        title = split[0]
        author = split[1]
        year = split[2]
        rating = messy_rating.strip("\n")
        new_book = Book(title, author, year, rating)
        temp_dict = {"title": new_book.get_title(),
                     "author": new_book.get_author(),
                     "year": new_book.get_year(),
                     "rating": new_book.get_rating()}
        book_list.append(temp_dict)
    all_books.close()


def make_a_book(t, a, y, r):  # this function makes a book in the form of a dictionary
    if type(t) == str:
        if type(a) == str:
            if 0 < int(y) < 2023:
                if 0 <= float(r) <= 5:
                    new_book = Book(t, a, y, r)
                else:
                    raise Exception("Rating must be an integer between 0 and 5")
            else:
                raise Exception("Year must be an integer less than 2023")
        else:
            raise Exception("Author must be a string")
    else:
        raise Exception("Title must be a string")
    return new_book


def add_book(cs):  # this function takes user input and makes a book in the form of a dictionary, then writes the
    # book to a csv file
    temp_list = []
    t = input("What is the book's name?: ")
    a = input("What is the book's author?: ")
    y = input("What is the book's publication year?: ")
    r = input("What is the book's rating?: ")
    book = make_a_book(t, a, y, r)
    temp_list.append(book.get_title())
    temp_list.append(book.get_author())
    temp_list.append(book.get_year())
    temp_list.append(book.get_rating())
    all_books = open(cs, "a")
    pen = csv.writer(all_books)
    pen.writerow(temp_list)
    print(f"{t} ({y}) by {a} -- Rating = {r} is added")
    all_books.close()


def find_lowest_rating():  # this function finds the lowest rating
    global lowest, lowest_year, lowest_author, lowest2_year, lowest2_author
    lowest_score = 2 ** 32
    lowest2 = None
    for book in book_list:
        rating = book.get('rating')
        title = book.get('title')
        if float(rating) < float(lowest_score):
            lowest = book.get('title')
            lowest_score = book.get('rating')
            lowest_author = book.get('author')
            lowest_year = book.get('year')
        if float(rating) == float(lowest_score) and title != lowest:
            lowest2 = book.get('title')
            lowest2_author = book.get('author')
            lowest2_year = book.get('year')
    print("The book(s) with the lowest rating are:")
    print(f"{lowest} ({lowest_year}) by {lowest_author} -- Rating = {lowest_score}")
    if lowest2 is not None:
        print(f"{lowest2} ({lowest2_year}) by {lowest2_author} -- Rating = {lowest_score}")


def find_highest_rating():  # this function finds the highest rating
    global highest
    highest_score = -(2 ** 32)
    for book in book_list:
        rating = book.get('rating')
        title = book.get('title')
        if float(rating) > float(highest_score):
            highest = (f"{book.get('title')} ({book.get('year')}) by {book.get('author')} -- Rating = {book.get('rating')}")
            highest_score = book.get('rating')
        if float(rating) == float(highest_score) and title != highest:
            highest = (str(highest) + "\n" + f"{book.get('title')} ({book.get('year')}) by {book.get('author')} -- Rating = {book.get('rating')}")
    print("The book(s) with the highest rating are:")
    print(highest)


def choices(cs):  # this function outlines the choices the user can take, and executes the corresponding functions
    cont = True
    while cont:
        choice = input("What operation would you like to do? ('highest rating', 'lowest rating', 'add book', 'done'): ")
        if choice == "highest rating":
            find_highest_rating()
        if choice == "lowest rating":
            find_lowest_rating()
        if choice == "add book":
            add_book(cs)
        if choice == "done":
            cont = False
            book_list.clear()


def main():
    want_to_continue = True
    while want_to_continue:
        try:
            cs = input("What csv file would you like to analyze?: ")
            parser(cs)
            choices(cs)
            switch = input("Would you like to process another file? (y/n): ")
            if switch != "y":
                want_to_continue = False
                print("Thank you for a great semester! I learned a lot!")
        except ValueError:
            print("There was a ValueError; make sure you are entering the right file type (***.csv)")
        except IOError:
            print("There was an IOError; make sure you are entering a file that exists")


main()
