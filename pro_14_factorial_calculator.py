# factorial calculator
# calculates factorial using loop
# also shows step by step calculation


while True:

    print("\n1 calculate factorial")
    print("2 exit")

    ch = input("enter choice: ")

    # exit option
    if ch == "2":
        print("exited")
        break

    elif ch == "1":

        n = int(input("enter number: "))

        # negative number case
        if n < 0:
            print("factorial not possible for negative numbers")
            continue

        # factorial of 0 is always 1
        if n == 0:
            print("0! = 1")
            continue

        fact = 1
        steps = ""

        # calculating factorial
        for i in range(n, 0, -1):
            fact *= i
            steps += str(i)
            if i != 1:
                steps += " x "

        print(f"\n{n}! = {steps} = {fact}")

    else:
        print("wrong choice. try again")