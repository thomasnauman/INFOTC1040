class Student:
    # private attributes
    # are only visible inside the class definition
    __first_name = None
    last_name = None
    age = 0
    house = None

    def __init__(self, f, l, a, h):
        self.__first_name = f
        self.last_name = l
        self.age = a
        self.house = h
    # function is public, and inside the class definition, so it can return a private attribute
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_house(self):
        return self.house

    def set_first_name(self, f):
        self.__first_name = f
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
        return f"{self.__first_name} {self.last_name}, {self.age} years old, is in House {self.house}"

    def change_house(self, new_house):
        self.house = new_house
        print(f"{self.__first_name} changed to house {new_house}")