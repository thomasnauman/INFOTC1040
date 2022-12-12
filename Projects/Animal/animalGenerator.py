from Animal import Animal

animal_list = []


def animal_maker():
    a_type = input("What type of animal would you like to create?: ")
    name = input("What is the animal’s name?: ")
    mood = input(f"How is {name} feeling?: ")
    animal = Animal(a_type, name, mood)
    animal_list.append(animal)
    return animal


def animal_lister():
    print("Animal List")
    for animal in animal_list:
        print(f"{animal.get_name()} the {animal.get_animal_type()} is feeling {animal.get_mood()}")
    print("Thanks!")


def main():
    make_an_animal = True
    while make_an_animal:
        print("Welcome to the animal generator!")
        print("This program creates Animal objects.")
        animal_maker()
        status = input("Would you like to add more animals (y/n)?: ")
        if status != "y":
            make_an_animal = False
            animal_lister()


main()
