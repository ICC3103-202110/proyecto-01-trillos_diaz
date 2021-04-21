from card import Card



class Ambassador(Card):
    def __init__(self,cardID,cardStatus="hidden",cardCost=0,cardType="Ambassador"):
        super(Ambassador,self).__init__(cardID,cardStatus,cardCost,cardType)

    #def gameplay(self):