# "in" operator
# returns a boolean value
numbers = [1, 2, 5, 6, -10]
#for number in numbers:
    #print(number)

#print(10 in numbers)
# if we only use "in", it will return a boolean value: is 10 inside the numbers list? False (it is not).
#print(5 in numbers)

def finder(element, list):
    if element in list:
        print("Found it!")
    else:
        print("I can't find it")

#finder(10, numbers)
#finder(-10, numbers)

def index_of(element, list):
    i = 0
    for x in list:
        if x == element:
            print(x, "is in the list at index", i)
            break
        else:
            print("Not here")
            i += 1

#index_of(10, numbers)
index_of(5, numbers)
#index_of(10, numbers)
#index_of(2, numbers)



