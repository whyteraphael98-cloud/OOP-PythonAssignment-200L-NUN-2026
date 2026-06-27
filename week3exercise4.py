balance = 1000
    
while True:
    print("\nATM Menu")
    print("1 Check balance")
    print("2 Deposit money")
    print("3 Withdraw money")
    print("4 Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        print(f"Your current balance is: N{balance}")
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Deposited N{amount:.2f}. New balance: N{balance:.2f}")
        else:
            print("Please enter a positive amount.")
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= 0:
            print("Please enter a positive amount.")
        elif amount > balance:
            print("Insufficient funds. Withdrawal rejected.")
        else:
            balance -= amount
            print(f"Withdrew N{amount:.2f}. New balance: N{balance:.2f}")
    elif choice == "4":
        print("Exiting. Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3 or 4.")
