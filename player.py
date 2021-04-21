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

    def gameStatus(self):
        print("yeet")
        print(self.__card1.cardStatus)
        if self.__card1.cardStatus == "hidden" and self.__card2.cardStatus == "hidden":
            self.__isInGame = 0

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


    def Getincome(self):
        self.__coins += 1
        print(self.coins)
    
    def GetForeignAid(self):
        self.__coins += 2
        print(self.coins)

    
    

    def DoCoup(self):
        num = int(self.number)
        print(num)
        self.__coins -= 7
        gamer=0
        while(gamer==0):
            gamer = input("Select which player you want to perform the COUP: ")
            print(gamer)
            if(gamer==num):
                print("Please select again a Player")
                gamer = 0
            elif(gamer!=0):
                return gamer
                
    def SeeCoins(self):
        print(self.__coins)
    
    def cardCoinCost(self,cardnum):
        if cardnum == 1:
            print(self.__card1.cardCost)
        else:
            print(self.__card1.cardCost)

    def SeeCards(self):
        print(self.__card1)
        print(self.__card2)



    def canDoRial(self):
        cardIds=[self.__card1.cardIDShow(),self.__card2.cardIDShow()]
        return cardIds

    
    def CurrentPlayer(self):
        return self.number


            







