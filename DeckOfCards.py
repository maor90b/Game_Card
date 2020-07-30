from Game_Cards.Card import Card
from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.deck =[]
        values=[i for i in range(2,15)]
        suits=['Diamond','Spade','Heart','Club']
        for i in values:
            for j in suits:
                self.deck.append(Card(j, i))


    # def __repr__(self):
    #     return self.deck

    def __shuffle(self):
        shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()


    def new_game(self):
        self.__init__()
        self.__shuffle()

    def show(self):
        print(self.deck)






























