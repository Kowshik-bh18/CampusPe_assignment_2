# statistical analysis program
# calculates sum, average, max, min, median and mode


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

        # avoids division error
        if n <= 0:
            print("please enter number greater than 0")
            continue

        nums = []

        # taking numbers
        for i in range(n):
            value = float(input(f"enter number {i+1}: "))
            nums.append(value)

        # basic calculations
        total = sum(nums)
        average = total / n
        maximum = max(nums)
        minimum = min(nums)

        # median calculation
        nums.sort()
        if n % 2 == 1:
            median = nums[n // 2]
        else:
            median = (nums[n//2 - 1] + nums[n//2]) / 2

        # mode calculation
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_count = max(freq.values())
        mode = [k for k, v in freq.items() if v == max_count]

        print("\n--- result ---")
        print("sum:", total)
        print("average:", round(average, 2))
        print("maximum:", maximum)
        print("minimum:", minimum)
        print("median:", median)

        if len(mode) == len(nums):
            print("mode: no mode")
        else:
            print("mode:", mode)

    else:
        print("wrong choice. try again")