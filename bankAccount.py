class BankAccount:

  def __init__(self, account_number, owner, balance=0.0):
    self.account_number = account_number
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      print(f"Deposited ${amount}. New balance: ${self.balance}")
    else:
      print("Invalid deposit amount.")

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      print(f"Withdrew ${amount}. New balance: ${self.balance}")
    else:
      print("Insufficient funds or invalid withdrawal amount.")

  def get_balance(self):
    print(f"Account balance for {self.owner}: ${self.balance}")

  def __str__(self):
    return f"Account Number: {self.account_number}\nOwner: {self.owner}\nBalance: ${self.balance}"


# Create bank accounts
account1 = BankAccount(1, "Alice")
account2 = BankAccount(2, "Bob")

while True:
  print("\nOptions:")
  print("1. Deposit")
  print("2. Withdraw")
  print("3. Check Balance")
  print("4. Quit")

  choice = input("Enter your choice: ")

  if choice == "1":
    amount = float(input("Enter the deposit amount: $"))
    account1.deposit(amount)
  elif choice == "2":
    amount = float(input("Enter the withdrawal amount: $"))
    account1.withdraw(amount)
  elif choice == "3":
    account1.get_balance()
  elif choice == "4":
    print("Goodbye!")
    break
  else:
    print("Invalid choice. Please try again.")
