import random
from card import Card
from ambassador import Ambassador
from assasin import Assasin
from captain import Captain
from contessa import Contessa
from duke import Duke

class Deck():
    def __init__(self,playercount):
        self.playercount = playercount
    
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
        deck=[ambas1,ambas2,ambas3,assasin1,assasin2,assasin3,captain1,captain2,captain3,contessa1,contessa2,contessa3,duke1,duke2,duke3]
        random.shuffle(deck)
        duke1.cardprint()
        print(deck)
        
    
    #def RandomizeCards(self):
        #deck = cards
        #random.shuffle(deck)
        #return deck
 
        
lista=[]

bruh = Deck(4)
bruh.GenerateCards()
mazo = Card(lista)
