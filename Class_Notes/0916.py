# return of a function
# a function: takes inputs -> does something -> generates/returns an output
# whether to have a return or not: depends on if the function should give back some information

def get_input(place):
    operand = (input("Input the " + place))
    return operand

def calculate(input1, input2, operator):
    if operator == "+":
        result = input1 + input2
    elif operator == "-":
        result = input1 - input2
    elif operator == "*":
        result = input1 * input2
    elif operator == "/":
        result = input1 / input2
    else:
        print("Enter a valid operator!")
        result = "invalid"
    return result

def main():
    i1 = float(get_input("first number: "))
    i2 = float(get_input("second number: "))
    ope = get_input("operator? (+, -, *, or /): ")
    print("{} {} {} is".format(i1, ope, i2), calculate(i1, i2, ope))

main()