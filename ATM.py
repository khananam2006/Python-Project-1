balance = 1000

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        print(f"Your balance: ₹{balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{balance}")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{balance}")
        else:
            print("Insufficient balance!")
    elif choice == "4":
        print("Thank you for using the ATM.")
        break
    else:
        print("Invalid option. Try again.")