# class User():
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0

#     def make_depost(self, amount,):
#         self.account_balance += amount
#         return self
        
#     def make_withdrawl(self, amount):
#         self.account_balance -= amount
#         return self

#     def display_user_balance(self,):
#         print(f"user: {self.name}, Balance: ${self.account_balance} ")
#         return self

#     def transfer_money(self, other_user, amount):    
#         self.account_balance -= amount
#         other_user.account_balance += amount

class BankAccount:
    def __init__(self, int_rate=0, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def wirthdrawl(self, amount):
        if self.balance >= amount:
             self.balance -= amount
        else:
            self.balance -= 5
            print("Insufficient Funds Charging a $5 Fee")
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self


    def yield_interest(self):
         if self.balance > 0:
           self.balance = self.balance + self.balance * self.int_rate
         return self

ba1 = BankAccount(balance=100)
ba2 = BankAccount(.01,500)
        
ba1.deposit(100).deposit(50).deposit(50).wirthdrawl(300).yield_interest().display_account_info()
ba2.deposit(100).deposit(100).wirthdrawl(50).wirthdrawl(50).wirthdrawl(50).wirthdrawl(50).yield_interest().display_account_info()

# brandon = User("Brandon", "brandon@home.com")
# tom = User("Tom", "tom@home.com")
# myrla = User("Myrla", "myrla@home.com")

#brandon.make_depost(500).make_depost(800).make_depost(75).make_withdrawl(325).display_user_balance()

#tom.make_depost(750).make_depost(750).make_withdrawl(500).make_withdrawl(350).display_user_balance()

#myrla.make_depost(1250).make_withdrawl(250).make_withdrawl(150).make_withdrawl(325).display_user_balance()

# brandon.transfer_money(myrla,150)
# brandon.display_user_balance()
# myrla.display_user_balance()