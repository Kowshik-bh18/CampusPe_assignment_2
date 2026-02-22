# calculator using functions


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
        print("7 exit")

        ch = input("enter choice: ")

        # exit option
        if ch == "7":
            print("exited")
            break

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

        else:
            print("wrong choice..")


calculator()