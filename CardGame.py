from Game_Cards.DeckOfCards import DeckOfCards
from Game_Cards.Card import Card
from Game_Cards.Player import Player

class CardGame:
    def __init__(self,players=4):
        self.deck=DeckOfCards()
        self.players = players
        self.list_players=[]
        self.newGame()
        for i in range(players):
            p=Player(input('enter name: '))
            p.setHand(self.deck)
            self.list_players.append(p)

        # CardGame.newGame(deck)
        print(self.list_players)
    def newGame(self):
        self.deck.new_game()
        for i in range(len(self.list_players)):
            self.list_players[i].setHand(self.deck)


















