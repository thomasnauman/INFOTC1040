# Write a program that finds the maximum number in the list (of integers)
numbers = [1, 5, 7, -10, 6]
numbers_2 = []
def find_max_simple(list):
    print(max(list))

def find_max(list):
    if len(list) == 0:
        print("List is empty")

    else:
        largest = list[0]
        for number in list:
            if number > largest:
                largest = number
            else:
                pass
        print(largest)

find_max_simple(numbers)
find_max(numbers)
find_max(numbers_2)

