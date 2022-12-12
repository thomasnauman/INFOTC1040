# functions
# creating a calculator
# two jobs: addition and subtraction
# takes two operands and one operator

def get_input(place):
    operand = float(input("Input the " + place + " number: "))
    return operand

def calculate(input1, input2, operator):
    if operator == "+":
        return input1 + input2
    elif operator == "-":
        return input1 - input2
    elif operator == "*":
        return input1 * input2
    elif operator == "/":
        return input1 / input2
    else:
        print("Enter a valid operator!")
        return "invalid"

def main():
    input1 = get_input("first")
    input2 = get_input("second")
    operator = input("What is the operator? (+, -, *, or /): ")
    print("{} {} {} is".format(input1, operator, input2), calculate(input1, input2, operator))

main()

# parameters: in the header of the function
# arguments: when we call the function
# parameters should match arguments


