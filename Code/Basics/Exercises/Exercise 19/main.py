# Exercise 19: Python Banking Program

def show_balance(balance):
    print("*******************")
    print(f"Your balance is: ${balance:.2f}")
    print("*******************")
    print()

def deposit(balance):
    amount = float(input("How much money would you like to deposit? $"))
    if amount < 0:
        print("*******************")
        print("That is not a valid amount")
        print("*******************")
        print()
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much money would you like to withdraw? $"))
    if amount > balance:
        print("*******************")
        print("Insufficient funds")
        print("*******************")
        return 0
    elif amount < 0:
        print("*******************")
        print("amount must be greater than 0")
        print("*******************")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*******************")
        print("  Banking Program  ")
        print("*******************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print()
        print("*******************")
        choice = input("Enter your choice (1 - 4): ")
        print("*******************")
        
        match choice:
            case '1':
                show_balance(balance)
            case '2':
                balance += deposit(balance)
                print("*******************")
                print(f"Your balance is: ${balance:.2f}")
                print("*******************")
                print()
            case '3':
                balance -= withdraw(balance)
                print("*******************")
                print(f"Your balance is: ${balance:.2f}") 
                print("*******************")
                print()
            case '4':
                is_running = False
            case _:
                print("*******************")
                print("That is not a valid choice")
                print("*******************")
                print()
    
    print("*******************")
    print("Thank you! Have a nice day!")
    print("*******************")

if __name__ == '__main__':
    main()