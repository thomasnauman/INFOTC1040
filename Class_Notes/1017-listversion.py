# Object oriented programming

# hogwarts students
harry = {"first_name": "Harry", "last_name": "Potter", "age": 11, "house": "Gryffindor"}
ron = {"first_name": "Ron", "last_name": "Weasley", "age": 11, "house": "Gryffindor"}
cedric = {"first_name": "Cedric", "last_name": "Diggory", "age": 14, "house": "Hufflepuff"}

# using a function
def create_a_student():
    student = {}
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    age = int(input("Enter the age: "))
    house = input("Enter the house: ")
    student["first_name"] = first_name
    student["last_name"] = last_name
    student["age"] = age
    student["house"] = house
    return student

# draco = create_a_student()
# print(draco)

def simple_create(first, last, age, house):
    student = {}
    student["first_name"] = first
    student["last_name"] = last
    student["age"] = age
    student["house"] = house
    return student

luna = simple_create("Luna", "Lovegood", 10, None) # later Ravenclaw
print(luna)

# Each student is an object
# Each has four attributes
