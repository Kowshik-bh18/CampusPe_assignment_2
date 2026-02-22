# user enters how many numbers
# program calculates sum, average, max and min


while True:

    print("\n1 calculate")
    print("2 exit")

    ch = input("enter choice: ")

    # exit option
    if ch == "2":
        print("exited")
        break

    elif ch == "1":

        n = int(input("how many numbers you want to enter: "))

        # if user enters 0, avoids division error
        if n <= 0:
            print("please enter number greater than 0")
            continue

        nums = []

        # taking numbers one by one
        for i in range(n):
            value = float(input(f"enter number {i+1}: "))
            nums.append(value)

        total = sum(nums)
        average = total / n
        maximum = max(nums)
        minimum = min(nums)

        print("\n--- result ---")
        print("sum:", total)
        print("average:", round(average, 2))
        print("maximum:", maximum)
        print("minimum:", minimum)

    else:
        print("wrong choice. try again")
