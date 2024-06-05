def send_email():
    print("sending email notification")

def log():
    print("logging to log file")

class Bad_Bank_Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        """
            trying to everything in a single method
            not following doing one thing and only thing principle

            additional responsibilities taken-
                1) Logging the deposit transaction to a file
                2) Sending an email notification about the deposit
        """
        if amount <= 0:
            print("Error: Invalid deposit amount.")
            return False

        self.balance += amount

        # Logging the deposit transaction
        with open("transaction_log.txt", "a") as log_file:
            log_file.write(f"Deposit: {amount}, New Balance: {self.balance}\n")
        # Sending an email notification
        send_email()


class Bank_Account():
    def __init__(self,balance=0):
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            return False

        self.balance += amount
        return True

account = Bank_Account(1000)

amount_deposited = account.deposit(1000)
if amount_deposited:
    log()
    send_email()