# Tradition is, each class is in one file
#   Number of files = # of classes + 1
# Student class = Student.py
# House class = Class.py
# Driver code = main.py
# house:
# name
# head
# points

class House:
    name = None
    head = None
    points = 500

    def __init__(self, n, h):
        self.name = n
        self.head = h
        # self.points = p

    def __str__(self):
        return f"{self.name}"

    def get_name(self):
        return self.name
    def get_head(self):
        return self.head
    def get_points(self):
        return self.points

    def set_name(self, n):
        self.name = n
    def set_head(self, h):
        self.head = h
    def set_points(self, p):
        if p >= 0:
            self.points = p
        else:
            print("Points cannot be less than zero")

gryffindor = House("Gryffindor", "McGonagall")
slytherin = House("Slytherin", "Snape")
print(gryffindor)
print(slytherin)

class Student:
    # private attributes
    # are only visible inside the class definition
    __first_name = None
    last_name = None
    age = 0
    house = None

    def __init__(self, f, l, a, h):
        self.first_name = f
        self.last_name = l
        self.age = a
        self.house = h

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_house(self):
        return self.house

    def set_first_name(self, f):
        self.first_name = f
    def set_last_name(self, l):
        self.last_name = l
    def set_age(self, n):
        if n >= 0:
            self.age = n
        else:
            print("Age cannot be less than or equal to zero")
    def set_house(self, h):
        self.house = h

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, is in House {self.house}"

    def change_house(self, new_house):
        self.house = new_house
        print(f"{self.first_name} changed to house {new_house}")

def main():
    harry = Student("Harry", "Potter", 11, gryffindor)
    print(harry)
    harry.change_house(slytherin)
    print(harry)
    print(harry.__first_name)
main()

