

class Card():
    def __init__(self,cardID):
        self.__cardID = cardID


    
    @property
    def getid(self):
        return self.__cardID

    """
    @cardID.setter
    def cardID(self,newID):
        self.__cardID = newID
    """
    def cardprint(self):
        print(self.__cardID)
    