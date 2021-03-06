from card import Card

class Player():
    def __init__(self,number,coins,card1,card2):
        self.number = number
        self.__coins = coins
        self.__card1 = card1
        self.__card2 = card2
        self.__isInGame = 1


    @property
    def isInGame(self):
        return self.__isInGame

    @property
    def card1(self):
        return self.__card1
    
    @property
    def card2(self):
        return self.__card2

    def printCardType(self,cardToSee):
        if cardToSee == 1:
            return self.__card1.cardType
        else:
            return self.__card2.cardType


    def setCard(self,cardToAdd,cardToReplace):
        if cardToReplace == 1:
            self.__card1 = cardToAdd
        else:
            self.__card2 = cardToAdd

    def gameStatus(self):
        if self.__card1.cardStatus == "shown" and self.__card2.cardStatus == "shown":
            self.__isInGame = 0
            self.__coins = 0
            print("Player %d You lost all your influence!"%(self.number))

        else:
            print("Player %d Is still in game!"%(self.number))

    def cardStatusSet(self,cardToFlip):
        if (cardToFlip == 1) and (self.__card1.cardStatus =="hidden"):
            self.__card1.cardStatusChange()
            
        elif((cardToFlip == 2) and (self.__card2.cardStatus =="hidden")):
            self.__card2.cardStatusChange()
        else:
            self.gameStatus() 
        


    def specCardStatus(self,cardToSee):
        if cardToSee == 1:
            return self.__card1.cardStatus
        else:
            return self.__card2.cardStatus

    @property
    def coins(self):
        return self.__coins
    
    #@coins.setter
    def coinsChange(self,coinAmmount):
        self.__coins += coinAmmount


    def SeeCoins(self):
        print(self.__coins)
    
    def cardCoinCost(self,cardnum):
        if cardnum == 1:
            print(self.__card1.cardCost)
        else:
            print(self.__card2.cardCost)
        
    def SeeCards(self):
        print(self.__card1)
        print(self.__card2)


    def canDoRial(self):
        cardIds=[self.__card1.cardIDShow(),self.__card2.cardIDShow()]
        return cardIds

    
    def CurrentPlayer(self):
        return self.number


            







