# how do we read (from user keyboard) a bunch of numbers into a list?
# input()

def make_list():
    # for loop (or while loop)
    # we first need to know how many numbers the user wants to enter
    # = the length of the list eventually
    length = int(input("How many elements do you want in the list?: "))
    # create an empty list, keep adding elements to list (append, insert)
    numbers = []
    for index in range(length):
        numbers.append(float(input("Input number for slot " + str(index+1) + ": ")))
    print(numbers)

#make_list()

def read_list_file():
    numbers = open("/Users/thomasnauman/PycharmProjects/INFOTC1040/Class Notes/Files/0928_numbers", "r")
    number_list = []
    for number in numbers:
        split = number.split()
        for num in split:
            number_list.append(num)
    print(number_list)

read_list_file()



