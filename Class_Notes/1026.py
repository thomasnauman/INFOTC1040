from classes_Student import Student
from classes_House import House

points = {"Gryffindor": 500, "Slytherin": 650, "Hufflepuff": 450, "Ravenclaw": 500}
# global variable
all_houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]


def main():
    gryffindor = House("Gryffindor", "McGonagall")
    slytherin = House("Slytherin", "Snape")
    print(gryffindor)
    print(slytherin)

    harry = harry = Student("Harry", "Potter", 11, "Gryffindor")
    #ron = Student(10, 2.5, "Ron", "Mizzou")
    print(harry)
    #print(ron)
    # how do we make sure that nonsense entries like this don't get entered?
    # using the type() method

    # review of try-except
    try:
        n = float("cat")
    except:
        print("Cannot convert string to float")


    print(points["Gryffindor"])
    harry.punished(104)
    print(points["Gryffindor"])
main()