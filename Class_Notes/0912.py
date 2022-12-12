# try-except
def main():
    # let user input number
    while True:
        try:
            num = int(input("Input integer: "))
            remainder = num % 2
            if remainder == 1:
                print(num, "is odd")
            else:
                print(num, "is even")
            break
        except:
            print("Must print an integer")

main()

# loops
    # for-loops - not needed for module 4 challenge
    # while-loops
# while loops - needed for module 4 challenge

def while_loop(i):
    while i <= 10:
        print(i)
        i += 1

while_loop(1)

# while loop stops when i <= 10 is not True --  when it is boolean value False
# break: to break from a loop