# ways to import
#   module/library import
#       import math
#       print(math.pi)
#   Method 2
#       from math import pi
#       print(pi)

from classes_House import House
from classes_Student import Student

def main():
    gryffindor = House("Gryffindor", "McGonagall")
    slytherin = House("Slytherin", "Snape")
    print(gryffindor)
    print(slytherin)

    harry = Student("Harry", "Potter", 11, gryffindor)
    print(harry)
    harry.change_house(slytherin)
    print(harry)
    #print(harry.__first_name)
    print(harry.last_name)

main()