# calculator using functions

import math  # needed for square root


# addition function
def add(a, b):
    return a + b


# subtraction function
def subtract(a, b):
    return a - b


# multiplication function
def multiply(a, b):
    return a * b


# division function 
def divide(a, b):
    if b == 0:
        return "cannot divide by zero"
    return a / b


# modulus function
def modulus(a, b):
    return a % b


# power function
def power(a, b):
    return a ** b


# square root function
def square_root(a):
    if a < 0:
        return "no sqrt for negative number"
    return math.sqrt(a)


# percentage function
def percentage(a, b):
    return (a / 100) * b


# main calculator function
def calculator():

    while True:

        print("\n--- calculator menu ---")
        print("1 add")
        print("2 subtract")
        print("3 multiply")
        print("4 divide")
        print("5 modulus")
        print("6 power")
        print("7 square root")
        print("8 percentage")
        print("9 exit")

        ch = input("enter choice: ")

        if ch == "9":
            print("exited")
            break

        # sqrt needs only one input
        if ch == "7":
            a = float(input("enter number: "))
            print("result:", square_root(a))
            continue

        a = float(input("enter first number: "))
        b = float(input("enter second number: "))

        if ch == "1":
            print("result:", add(a, b))

        elif ch == "2":
            print("result:", subtract(a, b))

        elif ch == "3":
            print("result:", multiply(a, b))

        elif ch == "4":
            print("result:", divide(a, b))

        elif ch == "5":
            print("result:", modulus(a, b))

        elif ch == "6":
            print("result:", power(a, b))

        elif ch == "8":
            print("result:", percentage(a, b))

        else:
            print("wrong choice..")


calculator()