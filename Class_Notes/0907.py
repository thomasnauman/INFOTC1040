# review
import math
def calculate_perimeter(radius):
    # one block
    # everything inside this block can only see the "scope" of this block
    perimeter = 2 * math.pi * radius
    return perimeter

def main():
    # calculate the perimeter of a circle
    # 2*pi*r
    # 2*3.14*r
   # print("Input radius below:")
    radius = float(input("Input radius:"))
    # perimeter = 2 * 3.14159265358979 * radius
   # print(perimeter)
    print(calculate_perimeter(radius))

main()


# inputs
# conditionals and loops




