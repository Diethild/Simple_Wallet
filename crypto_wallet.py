class CryptoWallet:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: +{amount}")
            return True
        else:
            print("Amount must be greater than 0.")
            return False

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew: -{amount}")
            return True
        else:
            print("Insufficient balance.")
            return False

    def get_balance(self):
        return self.balance

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


def main():
    wallet = CryptoWallet()

    while True:
        print("\nCrypto Wallet Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Transactions")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            amount = float(input("Enter the amount to deposit: "))
            wallet.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter the amount to withdraw: "))
            wallet.withdraw(amount)
        elif choice == "3":
            print(f"Your balance is: {wallet.get_balance()}")
        elif choice == "4":
            print("Transaction history:")
            wallet.print_transactions()
        elif choice == "5":
            print("Exiting the wallet. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
