from card import Card

class Assasin(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=3,cardType="Assasin"):
        super(Assasin,self).__init__(cardID,cardStatus,cardCost,cardType)
