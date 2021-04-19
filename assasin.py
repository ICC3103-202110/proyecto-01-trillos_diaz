from card import Card

class Assasin(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=3):
        super(Assasin,self).__init__(cardID,cardStatus,cardCost)
    #def gameplay(self):

asss = Assasin(1)
print(asss.cardCost)