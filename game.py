from deck import Deck
from player import Player


class Game():
    def __init__(self,playerCount):
        self.playerCount = playerCount


    #def DoCardAction(self):
    #    print("Please select wich Card you want to perform")
    #    print("1:(Tax)\n2:(Assassinate)\n3:(Exchange)\n4:(Steal)\n")
    #    select = int(input())
    #   if(select==1):
    #        return 1
    #        
    #   if(select==2):
    #        return 2
    #       
    #    if(select==3):
    #       
    #       return 3
    #    if(select==4):
    #       return 4

    #def ChallengePlayer(self):
    #   pass
    #    if(self.__card1==self.compare):
    #       return 1
    #   elif(self.__card2==self.compare):
    #        return 1
    #    else:
    #        return 0


    def startGame(self):
        #start
        Ddeck = Deck()
        Ddeck.GenerateCards()
        print(Ddeck)
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player1 = Player(1,2,card11,card22)
        player1.SeeCards()
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player2 = Player(2,2,card11,card22)
        player2.SeeCards()
        card11 = Ddeck.takeCard()
        card22 = Ddeck.takeCard()
        player3 = Player(3,2,card11,card22)
        player3.SeeCards()
        if self.playerCount == 4:
            card11 = Ddeck.takeCard()
            card22 = Ddeck.takeCard()
            player4 = Player(4,2,card11,card22)
            player4.SeeCards()
        print("bruh")
        #player1.SeeCoins()
        #player1.coins()
        #player1.SeeCoins()
        player1.canDoRial()
        player1.cardCoinCost(1)
        return player1
        
        
