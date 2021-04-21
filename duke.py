from card import Card

class Duke(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=0,cardType="Duke"):
        super(Duke,self).__init__(cardID,cardStatus,cardCost,cardType)

    #def gameplay(self):