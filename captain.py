from card import Card

class Captain(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=3):
        super(Captain,self).__init__(cardID,cardStatus,cardCost)

    #def gameplay(self):