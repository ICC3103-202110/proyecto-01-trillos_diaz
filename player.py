from card import Card

class Player():
    def __init__(self,number,coins,card1,card2):
        self.number = number
        self.coins = coins
        self.__card1 = card1
        self.__card2 = card2

    #def getCoins(self,coinAmmount):
        #self.coins+=coinAmmount
    #@property
    #def coins(self):
        #return self.coins
    
    #@coins.setter
    #def coins(self,coinAmmount):
        #self.coins+=1


    def Getincome(self):
        self.coins += 1
        print(self.coins)
    
    def GetForeignAid(self):
        self.coins += 2
        print(self.coins)
    

    def DoCoup(self):
        num = int(self.number)
        print(num)
        self.coins -= 7
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
        print(self.coins)

    def SeeCards(self):
        print(self.__card1)
        print(self.__card2)

    def ChallengePlayer(self):
        pass
        #if():

        #if():

    def canDoRial(self):
        print(self.__card1.cardIDShow())
        print(self.__card2.cardIDShow())

    def DoCardAction(self):
        print("Please select wich Card you want to perform")
        print("1:(Tax)\n2:(Assassinate)\n3:(Exchange)\n4:(Steal)\n")
        select = int(input())
        if(select==1):
            print("uwu")
            return 1
            
        if(select==2):
            return 2
            
        if(select==3):
            
            return 3
        if(select==4):
            return 4
            



    #def gameplay(self):

#j1 = Player(1,2,"uwu","ewe")
#j1.DoCardAction()



