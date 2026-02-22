# temperature converter program
# menu based conversion between temperature scales
while True:
    print("1 c to f")
    print("2 f to c")
    print("3 c to k")
    print("4 k to c")
    print("5 exit")

    ch = input("choice: ")

    if ch == "1":
        c = float(input())
        print((c * 9/5) + 32)
    elif ch == "2":
        f = float(input())
        print((f - 32) * 5/9)
    elif ch == "3":
        c = float(input())
        print(c + 273.15)
    elif ch == "4":
        k = float(input())
        print(k - 273.15)
    elif ch == "5":
        break
