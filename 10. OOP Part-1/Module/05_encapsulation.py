class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner          # Public attribute
        self.__balance = initial_balance  # Private attribute (encapsulation)
    
    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")
    
    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")
    
    # Getter method for balance (read access)
    def get_balance(self):
        return self.__balance

    # Setter method for balance (write access)
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
            print("Balance updated successfully.")
        else:
            print("Invalid balance amount.")

# Using the encapsulated class
account = BankAccount("Alice", 1000)

# Accessing public attribute
print("Owner:", account.owner)

# Using public methods to interact with private attribute
account.deposit(500)     # Depositing money
print("Balance:", account.get_balance())  # Accessing balance through getter

account.withdraw(300)     # Withdrawing money
print("Balance:", account.get_balance())

# Updating balance through setter
account.set_balance(2000)
print("Balance after update:", account.get_balance())
