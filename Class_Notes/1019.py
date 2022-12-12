# object oriented programming
#   treat an entity as a whole object, each object has a bunch of attributes (properties)
#   There are methods that we can perform on each object

# Define classes -- a category of objects
# C++/Java tradition of naming classes with Capitals
class Student:
    # attributes
    first_name = None
    last_name = None
    age = 0
    house = None

    # important methods
    # method, function, procedure
    # initializer / constructors
    # specify or define the values of the attributes when you create a Student object

    # self refers to the current student I'm creating
    def __init__(self, f, l, n, h):
        # When we make a student object, we want the first name to be the "f" value
        self.first_name = f
        self.last_name = l
        if n < 0:
            print("Age cannot be negative. Invalid age.")
        else:
            self.age = n
        self.house = h

    # special function
    # tells Python how to represent student as a string
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old, is in House {self.house}"

    # Accessors
    # returns the values of attributes for an object
    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name
    def get_age(self):
        return self.age
    def get_house(self):
        return self.house

    # Mutators
    # modify attribute values
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


# create a student object
harry = Student("Harry", "Potter", 11, "Gryffindor")
print(type(harry))
#   this shows that his data type is "Student"

print(harry)
#   this prints where he is in the memory

print(harry.first_name)
#   this prints Harry's first name
print(harry.last_name)
print(harry.age)
print(harry.house)

# safer / less error prone than using a dictionary
ron = Student("Ron", "Weasley", -10, "Gryffindor")
print(ron.age)
ron = Student("Ron", "Weasley", 10, "Gryffindor")
print(ron.age)
print(ron)

print(ron.age)
print(ron.get_age())
# This returns the same thing

harry.set_age(12)
print(harry)
# This changed his age to 12 years old

harry.set_age(-2)
print(harry)
# Using the mutator, we cannot change his age to -2

harry.age = -2
print(harry)
# Directly modifying, we are able to do this
harry.age = 11
