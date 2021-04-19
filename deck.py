import random
from card import Card
from player import Player
from ambassador import Ambassador
from assasin import Assasin
from captain import Captain
from contessa import Contessa
from duke import Duke

class Deck():
    def __init__(self,playerCount):
        self.playerCount = playerCount
        self.cardDeck = []
    
    def GenerateCards(self):
        ambas1 = Ambassador(1)
        ambas2 = Ambassador(2)
        ambas3 = Ambassador(3)
        assasin1 = Assasin(4)
        assasin2 = Assasin(5)
        assasin3 = Assasin(6)
        captain1 = Captain(7)
        captain2 = Captain(8)
        captain3 = Captain(9)
        contessa1 = Contessa(10)
        contessa2 = Contessa(11)
        contessa3 = Contessa(12)
        duke1 = Duke(13)
        duke2 = Duke(14)
        duke3 = Duke(15)
        self.cardDeck=[ambas1,ambas2,ambas3,assasin1,assasin2,assasin3,captain1,captain2,captain3,contessa1,contessa2,contessa3,duke1,duke2,duke3]
        #print(ambas1.cardStatusShow())
        """
        deckid=[ambas1.cardStatusShow(),ambas2.cardStatusShow(),ambas3.cardStatusShow(),assasin1.cardStatusShow()
        ,assasin2.cardStatusShow(),assasin3.cardStatusShow(),captain1.cardStatusShow(),captain2.cardStatusShow()
        ,captain3.cardStatusShow(),contessa1.cardStatusShow(),contessa2.cardStatusShow(),contessa3.cardStatusShow(),duke1.cardStatusShow(),duke2.cardStatusShow(),duke3.cardStatusShow()]
        """
        random.shuffle(self.cardDeck)
        #random.shuffle(deckid)
        #duke1.cardprint()
        #print(self.cardDeck)
        #print(deckid)
        
    def takeCard(self):
        curcard = self.cardDeck[0]
        self.cardDeck.pop(0)
        return curcard

    def replaceCard(self,card2replace):
        curcard = self.cardDeck[0]
        self.cardDeck.pop(0)
        self.cardDeck.append(card2replace)
        print(curcard)
        return curcard
    
    def startGame(self):
        card11 = self.takeCard()
        card22 = self.takeCard()
        player1 = Player(1,2,card11,card22)
        player1.SeeCards()
        card11 = self.takeCard()
        card22 = self.takeCard()
        player2 = Player(2,2,card11,card22)
        player2.SeeCards()
        card11 = self.takeCard()
        card22 = self.takeCard()
        player3 = Player(3,2,card11,card22)
        player3.SeeCards()
        if self.playerCount == 4:
            card11 = self.takeCard()
            card22 = self.takeCard()
            player4 = Player(4,2,card11,card22)
            player4.SeeCards()
        player1.SeeCoins()
        player1.Getincome()
        player1.SeeCoins()

    #def RandomizeCards(self):
        #deck = cards
        #random.shuffle(deck)
        #return deck
 
lista=[]

bruh = Deck(4)
bruh.GenerateCards()
mazo = Card(lista)

bruh.startGame()
#aaaa = bruh.takeCard()
