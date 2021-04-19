import random
from card import Card
from player import Player
from ambassador import Ambassador
from assasin import Assasin
from captain import Captain
from contessa import Contessa
from duke import Duke

class Deck():
    def __init__(self):
    
        self.cardDeck = []
    
    def GenerateCards(self):
        ambas1 = Ambassador(1)
        ambas2 = Ambassador(1)
        ambas3 = Ambassador(1)
        assasin1 = Assasin(2)
        assasin2 = Assasin(2)
        assasin3 = Assasin(2)
        captain1 = Captain(3)
        captain2 = Captain(3)
        captain3 = Captain(3)
        contessa1 = Contessa(4)
        contessa2 = Contessa(4)
        contessa3 = Contessa(4)
        duke1 = Duke(5)
        duke2 = Duke(5)
        duke3 = Duke(5)
        self.cardDeck=[ambas1,ambas2,ambas3,assasin1,assasin2,assasin3,captain1,captain2,captain3,contessa1,contessa2,contessa3,duke1,duke2,duke3]
        #print(ambas1.cardStatusShow())
        """
        deckid=[ambas1.cardStatusShow(),ambas2.cardStatusShow(),ambas3.cardStatusShow(),assasin1.cardStatusShow()
        ,assasin2.cardStatusShow(),assasin3.cardStatusShow(),captain1.cardStatusShow(),captain2.cardStatusShow()
        ,captain3.cardStatusShow(),contessa1.cardStatusShow(),contessa2.cardStatusShow(),contessa3.cardStatusShow(),duke1.cardStatusShow(),duke2.cardStatusShow(),duke3.cardStatusShow()]
        """
        random.shuffle(self.cardDeck)
        #print(self.cardDeck)
        #random.shuffle(deckid)
        #duke1.cardprint()
        #print(self.cardDeck)
        #print(deckid)
        return self.cardDeck
        
    def takeCard(self):
        #print("yeet")
        curcard = self.cardDeck[0]
        self.cardDeck.pop(0)
        return curcard

    def replaceCard(self,card2replace):
        curcard = self.cardDeck[0]
        self.cardDeck.pop(0)
        self.cardDeck.append(card2replace)
        print(curcard)
        return curcard
    
    

    #def RandomizeCards(self):
        #deck = cards
        #random.shuffle(deck)
        #return deck
 
