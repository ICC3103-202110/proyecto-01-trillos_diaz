    

class Player():
    def __init__(self,number,coins,card1,card2):
        self.number = number
        self.coins = coins
        self.__card1 = card1
        self.__card2 = card2

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


    #def gameplay(self):





