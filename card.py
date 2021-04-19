

class Card():
    def __init__(self,cardID):
        self.__cardID = cardID
        self.__cardStatus = "hidden"

    @property
    def cardID(self):
        return self.__cardID

    
    def cardIDSet(self,newID):
        self.__cardID = newID

    @property
    def cardStatus(self):
        return self.__cardStatus

    def cardStatusSet(self):
        print("yeet")
        if self.__cardStatus == "hidden":

            self.__cardStatus = "shown"

    def cardprint(self):
        print(self.__cardID)
    
    def cardStatusShow(self):
        print(self.__cardStatus)

card1 = Card(1)
card1.cardStatusShow()
card1.cardStatusSet()
card1.cardStatusShow()

    