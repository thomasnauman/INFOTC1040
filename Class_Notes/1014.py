# try/except
"""n = float(input("Please enter number: "))
n2 = n + 2
print(n2)"""
# what if we enter a string?
# try/except!

try:
    n = float(input("Please enter number: "))
    n2 = n + 2
    print(n2)
#except:
    #print("Error")

# purpose of using try except
#   not for getting rid of bugs! Instead of returning error, it just stops!

# except: if something goes wrong, execute this part

# raise an exception only where there is NameError:
except NameError:
    print("There is a NameError")
except ValueError:
    print("There is a ValueError")

# optional
# else block: this code executes if there was no errors whatsoever
else:
    print("Everything worked fine")

# finally block: executes no matter what happens

finally:
    print("Execution finished")

"""
try:
    your code
except ErrorType:
    execute this part if something goes wrong
else: 
    execute this part if nothing goes wrong
finally:
    execute this part no matter what happens
    """


