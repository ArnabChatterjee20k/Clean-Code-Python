# Methods Responsibility

### good methods
Methods should do one thing only. If you have to run an action and then
check for the status, so that in separate methods that are called by
different statements.

### "doing one thing and one thing only" ?
* The principle of "doing one thing and one thing only" refers to the main responsibility or concern of a method or function. If a method's primary responsibility is to modify the state of an object, and it also provides feedback on the success or failure of that operation through a returned status or result, it can be considered as having a single, well-defined responsibility.

* However, it is important to ensure that the method does not inadvertently take on additional responsibilities beyond its primary purpose. If the method starts performing other unrelated tasks or calculations, it may violate the single responsibility principle and become harder to maintain and test.

### Command and query separation
* The command and query separation principle is a design guideline in object-oriented programming that suggests separating methods that modify the state of an object (commands) from those that only return data (queries).

* It should follow "doing one thing and one thing only" principle

### Bad code
```python
def send_email():
    print("sending email notification")

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

```

### Good code
```python
def send_email():
    print("sending email notification")

def log():
    print("logging to log file")
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
```