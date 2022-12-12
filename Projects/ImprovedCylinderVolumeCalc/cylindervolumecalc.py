import math


def calculate_volume(radius, height):
    volume = math.pi * radius ** 2 * height
    return volume


def main():
    do_a_calculation = True
    while do_a_calculation:
        radius = float(input("Enter the radius: "))
        if radius < 0:
            print("Please enter a positive value and try again!")
        else:
            height = float(input("Enter the height: "))
            if height < 0:
                print("Please enter a positive value and try again!")
            else:
                print("The volume of a cylinder with height {} and radius {} is".format(str(height), str(radius)),
                      calculate_volume(radius, height))
                repeat = input("Would you like to do another calculation?: ")
                if repeat != "y":
                    do_a_calculation = False
                    print("Thank you for calculating!")


main()
