class BankAccount:
  def __init__(self, account_holder, balance=0):
      self.account_holder = account_holder
      self.balance = balance

  def deposit(self, amount):
      if amount > 0:
          self.balance += amount
          print(f"Deposited ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid deposit amount. Please enter a positive amount.")

  def withdraw(self, amount):
      if 0 < amount <= self.balance:
          self.balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.balance}")
      else:
          print("Invalid withdrawal amount. Please check your balance and enter a valid amount.")


account = BankAccount("John Doe")

account.deposit(1000)
account.withdraw(500)

account.deposit(-200)
account.withdraw(2000)
