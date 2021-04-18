import random

class Card():
    def __init__(self,cards):
        self.cards = cards
    
    def GenerateCards(self):
        deck=[1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
        random.shuffle(deck)
        return deck
    
    def RandomizeCards(self):
        deck = self.cards
        random.shuffle(deck)
        return deck
        
lista=[]
mazo = Card(0)
lista= mazo.GenerateCards()
mazo = Card(lista)
print(lista)
lista = mazo.RandomizeCards()
print(lista)