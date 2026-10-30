balance = 10000

def check_balance():
    print("Available balance is", balance)

def deposit():
    global balance
    amount = int(input("Enter deposit amount: "))
    if amount > 0:
        balance += amount
        print("Deposit successful")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = int(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient amount")
    else:
        balance -= amount
        print("Withdrawal successful")

while True:
    print("\n1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    a = int(input("Enter your choice: "))

    if a == 1:
        check_balance()
    elif a == 2:
        deposit()
    elif a == 3:
        withdraw()
    elif a == 4:
        print("Thank you!")
        break
    else:
        print("Invalid choice")
