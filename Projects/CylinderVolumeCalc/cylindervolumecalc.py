import math
def calculate_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume

def main():
    radius = float(input("Enter the radius: "))
    height = float(input("Enter the height: "))
    if radius > 0:
        print("The volume of a cylinder with height {} and radius {} is".format(str(height), str(radius)),calculate_volume(radius, height))
    else:
        print("Please enter a positive value and try again!")
main()

