class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_depost(self, amount):
        self.account_balance += amount
        
    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"user: {self.name}, Balance: ${self.account_balance} ")

    def transfer_money(self, other_user, amount):  # I can not get the transfer function to work properly. I will keep working on it
        other_user.account_balance += amount
        self.account_balance -= amount


brandon = User("Brandon", "brandon@home.com")
tom = User("Tom", "tom@home.com")
myrla = User("Myrla", "myrla@home.com")

# brandon.make_depost(500)
# brandon.make_depost(800)
# brandon.make_depost(75)
# brandon.make_withdrawl(325)
# brandon.display_user_balance()

# tom.make_depost(750)
# tom.make_depost(750)
# tom.make_withdrawl(500)
# tom.make_withdrawl(350)
# tom.display_user_balance()

# myrla.make_depost(1250)
# myrla.make_withdrawl(250)
# myrla.make_withdrawl(150)
# myrla.make_withdrawl(325)
# myrla.display_user_balance()

brandon.transfer_money(myrla,150)
brandon.display_user_balance()
myrla.display_user_balance()