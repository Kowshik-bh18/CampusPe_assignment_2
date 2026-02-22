# number system functions


# factorial function
def factorial(n):
    if n < 0:
        return "not defined for negative numbers"
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


# prime check function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# fibonacci function (nth fibonacci)
def fibonacci(n):
    if n <= 0:
        return "enter positive number"
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return a


# sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))


# reverse number
def reverse_number(n):
    return int(str(n)[::-1])


# armstrong number check
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    total = sum(int(d)**power for d in digits)
    return total == n


# gcd function (euclidean method)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# lcm function
def lcm(a, b):
    return abs(a*b) // gcd(a, b)


# perfect number check
def is_perfect_number(n):
    if n <= 0:
        return False
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n


# main menu function
def math_menu():

    while True:

        print("\n--- math menu ---")
        print("1 factorial")
        print("2 prime check")
        print("3 fibonacci")
        print("4 sum of digits")
        print("5 reverse number")
        print("6 armstrong check")
        print("7 gcd")
        print("8 lcm")
        print("9 perfect number check")
        print("10 exit")

        ch = input("enter choice: ")

        if ch == "10":
            print("exited")
            break

        elif ch == "1":
            n = int(input("enter number: "))
            print("result:", factorial(n))

        elif ch == "2":
            n = int(input("enter number: "))
            print("prime:", is_prime(n))

        elif ch == "3":
            n = int(input("enter n: "))
            print("fibonacci:", fibonacci(n))

        elif ch == "4":
            n = int(input("enter number: "))
            print("sum of digits:", sum_of_digits(n))

        elif ch == "5":
            n = int(input("enter number: "))
            print("reversed:", reverse_number(n))

        elif ch == "6":
            n = int(input("enter number: "))
            print("armstrong:", is_armstrong(n))

        elif ch == "7":
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
            print("gcd:", gcd(a, b))

        elif ch == "8":
            a = int(input("enter first number: "))
            b = int(input("enter second number: "))
            print("lcm:", lcm(a, b))

        elif ch == "9":
            n = int(input("enter number: "))
            print("perfect number:", is_perfect_number(n))

        else:
            print("wrong choice. try again")


# run program
math_menu()