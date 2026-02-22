# number guessing game
# added difficulty levels (easy, medium, hard)


import random

best_score = None


while True:

    # choose difficulty level
    print("\nchoose difficulty:")
    print("1 easy (1-50)")
    print("2 medium (1-100)")
    print("3 hard (1-1000)")

    level = input("enter choice: ")

    if level == "1":
        low, high = 1, 50
    elif level == "2":
        low, high = 1, 100
    elif level == "3":
        low, high = 1, 1000
    else:
        print("wrong choice")
        continue

    num = random.randint(low, high)
    attempts = 7
    used = 0

    print(f"\nguess number between {low}-{high}")

    while attempts > 0:

        g = int(input("guess: "))
        used += 1
        attempts -= 1

        if g == num:
            print("correct ")
            print("attempts used:", used)

            # update best score
            if best_score is None or used < best_score:
                best_score = used
                print("new best score:", best_score)

            break

        elif g > num:
            print("too high")

        else:
            print("too low")

        # close hint
        if abs(g - num) <= 5:
            print("very close ")

        print("attempts left:", attempts)

    else:
        print("you lost ")
        print("number was:", num)

    again = input("\nplay again? (y/n): ").lower()
    if again != "y":
        print("thanks for playing")
        break