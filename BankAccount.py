# Defined BankAccount Class.
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.full_name = full_name
        self.account_number = account_number
        self.routing_number = routing_number
        self.balance = balance

# Defined Deposit.
    def deposit(self, amount):
        self.balance += amount
        print(f"Amount Deposited: ${amount}")

# Defined Withdraw.
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Amount Withdrawn: ${amount}")
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10

# Defined Get_Balance.
    def get_balance(self):
        print(f"Balance: ${self.balance}")

# Defined Add_Interest.
    def add_interest(self):
        balance = self.balance
        interest = balance * 0.00083
        self.balance = self.balance + interest

# Defined Print_Receipt.
    def print_receipt(self):
        stars = []

        for i in str(self.account_number):
            stars.append("*")
        str_account_num = str(self.account_number)
        stars[len(stars)-1] = str_account_num[len(stars)-1]
        stars[len(stars)-2] = str_account_num[len(stars)-2]
        stars[len(stars)-3] = str_account_num[len(stars)-3]
        stars[len(stars)-4] = str_account_num[len(stars)-4]

        str_stars = ""
        str_stars = str_stars.join(stars)
        print(f"""
            {self.full_name}
            Account No.: {str_stars}
            Routing No.: {self.routing_number}
            Balance: {self.balance}
        """)

# Account 1.
joi_account = BankAccount("Joi Anderson", 123456789, 987654321, 1234)
joi_account.get_balance()
joi_account.add_interest()
joi_account.print_receipt()

# Account 2.
alisher_account = BankAccount("Alisher Begmatov", 123456789, 987654321, 1234)
alisher_account.withdraw(777)
alisher_account.deposit(21000)
alisher_account.print_receipt()

# Account 3.
user_account = BankAccount("User Account", 123456789, 987654321, 1234)
user_account.get_balance()
user_account.add_interest()
user_account.deposit(10000)
user_account.print_receipt()

# Alisher Begmatov.
