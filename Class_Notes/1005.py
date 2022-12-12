# dictionaries
# store records of students
# each student has an ID, first name, last name, age, house
# which datatype can we use to store this information?
    # lists, tuples
student_1 = [100, "Harry", "Potter", 15, "Gryffindor"]
student_2 = [101, "Draco", "Malfoy", 15, "Slytherin"]
all_students = [student_1, student_2]

# define a function that prints the information of a student given the ID
def print_student_info(id):
    for student in all_students:
        if id == student[0]:
            print(student[1],student[2],"is",str(student[3]),"years old and in house",student[4])
        else:
            pass

#print_student_info(101)

# we want to delete the age info from every student
for student in all_students:
    del student[3]

#print(student_1)
#print(student_2)

#print_student_info(100)

def new_student_info(id):
    for student in all_students:
        if id == student[0]:
            print(student[1],student[2],"is in house",student[3])
        else:
            pass

#new_student_info(100)

# dictionaries!
# elements are still separated by commas, but there are also colons now
# key:element pairs
# key -- index, value -- element
# keys are almost like named indices

dictstudent1 = {"id": 100,
                "name": "Harry",
                "lastname": "Potter",
                "age": 15,
                "house": "Gryffindor"}
dictstudent2 = {"id": 101,
                "name": "Draco",
                "lastname": "Malfoy",
                "age": 15,
                "house": "Slytherin"}
all_dict_students = [dictstudent1, dictstudent2]
def print_dict_student_info(id):
    for student in all_dict_students:
        if student["id"] == id:
            print(student["name"],student["lastname"],"is",str(student["age"]),"years old and in house",student["house"])
        else:
            pass

print_dict_student_info(100)
print_dict_student_info(101)

# delete a key from a dictionary
for student in all_dict_students:
    del student["age"]

print(dictstudent1)
print(dictstudent2)

def new_print_dict_student_info(id):
    for student in all_dict_students:
        if student["id"] == id:
            print(student["name"],student["lastname"],"is in house",student["house"])
        else:
            pass

new_print_dict_student_info(100)
new_print_dict_student_info(101)
