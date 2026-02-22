# atm simulator program
# simple atm with deposit withdraw check balance

balance = 10000
MIN_BALANCE = 500

while True:
    print("\n===== ATM MENU =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        print(f"Current Balance: ₹{balance:.2f}")

    elif choice == "2":
        try:
            amount = float(input("Enter deposit amount: ₹"))
            if amount <= 0:
                print("Amount must be positive.")
            else:
                balance += amount
                print("Deposit successful.")
                print(f"Updated Balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid amount entered.")

    elif choice == "3":
        try:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount <= 0:
                print("Amount must be positive.")
            elif balance - amount < MIN_BALANCE:
                print("Cannot withdraw.")
                print(f"Minimum balance of ₹{MIN_BALANCE} must remain.")
            else:
                balance -= amount
                print("Withdrawal successful.")
                print(f"Remaining Balance: ₹{balance:.2f}")
        except ValueError:
            print("Invalid amount entered.")

    elif choice == "4":
        print("Thank you for using ATM.")
        break

    else:
        print("Invalid choice. Please try again.")