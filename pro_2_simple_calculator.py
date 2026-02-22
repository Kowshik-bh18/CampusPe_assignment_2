# simple calculator program
# this program performs basic arithmetic operations

try:
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    print("addition:", a + b)
    print("subtraction:", a - b)
    print("multiplication:", a * b)
    print("division:", a / b if b != 0 else "division by zero not allowed")
    print("modulus:", a % b if b != 0 else "division by zero not allowed")
    print("power:", a ** b)

except:
    print("invalid input")
