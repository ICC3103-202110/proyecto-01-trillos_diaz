

class Card():

    def __init__(self,cardID,cardStatus,cardCost,cardType):
        self.__cardID = cardID
        self.__cardStatus = cardStatus
        self.__cardCost = cardCost
        self.__cardType = cardType
        

    @property
    def cardID(self):
        return self.__cardID

    @property
    def cardType(self):
        return self.__cardType
    
    def cardIDSet(self,newID):
        self.__cardID = newID

    def cardIDShow(self):
        return self.__cardID

    @property
    def cardStatus(self):
        return self.__cardStatus

    def cardStatusChange(self):
        print(self.__cardStatus)
        self.__cardStatus ="shown"

    def cardprint(self):
        print(self.__cardID)
    
    def cardStatusShow(self):
        print(self.__cardStatus)

    @property
    def cardCost(self):
        return self.__cardCost
    
    

        

        

#card1 = Card(1)
#card1.cardStatusShow()
#card1.cardStatusSet()
#card1.cardStatusShow()

    