# review
import math
def calculate_perimeter(radius):
    perimeter = 2 * math.pi * radius
    return perimeter

def main():
    while True:
        radius = float(input("Input radius:"))
        if radius < 0:
            print("Enter a positive number.")
        else:
            perimeter = (calculate_perimeter(radius))
            print(perimeter)


main()





