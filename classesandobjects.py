#classes and objects
class Card:
    balance= 0
    def __init__(self,bal):
        self.balance=bal


    def withdraw (self,amount):
            if self.balance >= amount:
                self.balance-=amount+(0.20*amount)
                return "Withdrawal Success"
            else:
                return "insufficient bal"

def printReceipt(self,balance,withdraw):
    return  """"AMOUNT:.....{}
                 BALANCE:....{}
        """.format(withdraw,balance)

from classesandobjects import Card


card1= Card(4500)
my_card=Card(6000)

print(card1.balance)
print(card1.withdraw(2300))
print(card1.balance)


