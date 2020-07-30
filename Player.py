from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Card import Card
from random import randint



class Player:
    def __init__(self,name,money=randint(5000,10000),cards=5):
        self.cards=cards
        self.name=name
        self.money=money
        self.list_cards=[]

    def __repr__(self):
        return f'name: {self.name} money: {self.money} num cards: {self.cards} cards: {self.list_cards}'

    def setHand(self, deck):
        for i in range(self.cards):
            self.list_cards.append(deck.deal_one())

    def getCard(self):
        return self.list_cards.pop(randint(0,(len(self.list_cards))))

    def addCard(self,deck):
        self.list_cards.append(deck.deal_one())

    def reduceAmount(self,amount):
        self.money-=amount

    def addAmount(self,amount):
        self.money+=amount

    def print(self):
        print(f'name: {self.name}  money: {self.money}  cards: {self.list_cards}')

# p1=Player('maor',50)
# d=DeckOfCards()
# d.new_game()
# # dic1={}
# #
# # dic1[p1]=d
# # print(dic1)
#
#
# p1.print()
#
# p1.setHand(d)
# p1.print()
# p1.getCard()
# p1.print()
# p1.addCard(d)
# p1.print()
# p1.addAmount(200)
# p1.print()
#
















