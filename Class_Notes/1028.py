class Person:
    first_name = None
    last_name = None
    age = 0

    def __init__(self, f, l, a):
        self.first_name = f
        self.last_name = l
        self.age = a

    def __str__(self):
        return f"{self.__class__.__name__}: {self.first_name} is {self.age} years old"

# Student is a subclass of Person
# class ClassName(ParentClassName):
# subclass inherits everything in the Superclass
class Student(Person):
    house = None


    def __init__(self, f, l, a, h):
        """
        self.first_name = f
        self.last_name = l
        self.age = a
        self.house = h
        """
        super().__init__(f,l,a)
        self.house = h


    def __str__(self):
        return f"{self.__class__.__name__}: {self.first_name} is {self.age} years old and in House {self.house}"

def main():
    ron = Person("Ron", "Weasley", 13)
    print(ron)

    draco = Student("Draco", "Malfoy", 13, "Slytherin")
    print(draco)

main()