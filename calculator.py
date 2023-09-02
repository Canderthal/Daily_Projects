import os
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
calculating = True

while calculating:
    num1 = int(input("What is the first number?\n"))
    if num1 != int: #replace this if a specfic type of error occurs
        print("that was not a correct response.")
        num1 = int(input("What is the first number?\n"))
    for operations in functions:
        print(operations)
    operation = input("Which operation do you want to use?\n")
    num2 = int(input("what is the second number?\n"))
    if num2 != int: #replace this if a specfic type of error occurs
        print("that was not a correct response.")
        num2 = int(input("What is the first number?\n"))
    for operations in functions:
        if operation == operations:
            answer = functions[operation](num1, num2)
    print(f"{num1} {operation} {num2} = {answer}")
    cont = input(f"Do you want to continue with {answer}. y or n\n")
    rept_num = answer
    if cont == "n":
        calculating2 = False
    calculating2 = True
    while calculating2:
        if cont == "y":
            for operations in functions:
                print(operations)
            operation = input("Which operation do you want to use?\n")
            num2 = int(input("what is the second number?\n"))
            for operations in functions:
                if operation == operations:
                    answer = functions[operation](rept_num, num2)
            answer1 = answer
            print(f"{rept_num} {operation} {num2} = {answer1}")
            cont = input(f"Do you want to continue with {answer}. y or n\n")
            rept_num = answer1
        if cont == "n":
            calculating2 = False
            os.system('cls')
            break
        else:
            print("that was not a correct response.")
            cont = input(f"Do you want to continue with {answer}. y or n\n")
    

