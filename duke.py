from card import Card

class Duke(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=0):
        super(Duke,self).__init__(cardID,cardStatus,cardCost)

    #def gameplay(self):