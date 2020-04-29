class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_depost(self, amount, other_user):
        self.account_balance += amount
        return self
        
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self,):
        print(f"user: {self.name}, Balance: ${self.account_balance} ")
        return self

    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawl(amount)
        return self


brandon = User("Brandon", "brandon@home.com")
tom = User("Tom", "tom@home.com")
myrla = User("Myrla", "myrla@home.com")

#brandon.make_depost(500).make_depost(800).make_depost(75).make_withdrawl(325).display_user_balance()

#tom.make_depost(750).make_depost(750).make_withdrawl(500).make_withdrawl(350).display_user_balance()

#myrla.make_depost(1250).make_withdrawl(250).make_withdrawl(150).make_withdrawl(325).display_user_balance()

#brandon.transfer_money(myrla,150).display_user_balance()
#myrla.display_user_balance()