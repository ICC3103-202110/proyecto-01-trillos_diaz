from card import Card
from deck import Deck
from player import Player


class Game():
    def __init__(self,playerCount):
        self.playerCount = playerCount

    def startGame(self):
        Ddeck = Deck()
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player1 = Player(1,2,card11,card22)
        player1.SeeCards()
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player2 = Player(2,2,card11,card22)
        player2.SeeCards()
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player3 = Player(3,2,card11,card22)
        player3.SeeCards()
        if self.playerCount == 4:
            card11 = Ddeck.takeCard()
            card22 = Ddeck.takeCard()
            player4 = Player(4,2,card11,card22)
            player4.SeeCards()
        print("bruh")
        player1.SeeCoins()
        player1.coins()
        player1.SeeCoins()
        
