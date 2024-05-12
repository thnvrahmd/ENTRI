class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount {amount} deposited successfully. Your new balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully. Your new balance is {self.balance}")

    def check_balance(self):
        print(f"Your current balance is {self.balance}")


def main():
    # Creating a bank account
    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")
    account = BankAccount(account_number, pin)

    # Account login
    login_success = False
    while not login_success:
        entered_pin = input("Enter your PIN to login: ")
        if entered_pin == account.pin:
            login_success = True
            print("Login successful!\n")
        else:
            print("Incorrect PIN. Please try again.\n")

    # Banking operations
    while True:
        print("Choose an option:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Thank you for banking with us. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
