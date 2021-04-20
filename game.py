from deck import Deck
from player import Player


class Game():
    def __init__(self,playerCount,Players):
        self.playerCount = playerCount
        self.Players = Players


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
    
    def PlayerTurn(self):
        gamer = self.Players
        turn = gamer.CurrentPlayer()
        print("Player number %d it's your turn"%(turn))
        print("Player %d do you want to perform a Normal accion(Coin draw) or a card accion"%(turn))
        print("CARD ACTION = (0)\nNORMAL ACTION = (1)")
        select =int(input())
        if(select==0):
            print("\nPlease select wich Card Action you want to perform")
            print("TAX = (1)\nASSASSINATE = (2)\nEXCHANGE = (3)\nSTEAL = (4)\n")
            select = int(input())
            if(select==1):
                return 1
                
            if(select==2):
                return 2
            
            if(select==3):
            
                return 3
            if(select==4):
                return 4
        elif(select==1):
            print("Please Select wich Normal Action you want to perform")
            print("INCOME= (1)\n2:FOREING AID= (2)\n3:COUP = (3)")
            select = int(input())
            #if(select==1):
            

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
        
        Playerlist=[]
        Playerlist.append(player1)
        Playerlist.append(player2)
        Playerlist.append(player3)
        p_alive1 = 1
        p_alive2 = 1
        p_alive3 = 1
        if self.playerCount == 4:
            Playerlist.append(player4)
            p_alive4 = 1
        else:
            p_alive4 = 0

        ActiveGame = 1
        while(ActiveGame==1):
            if(p_alive1==1):
                current_game = Game(4,Playerlist[0])
                Action = current_game.PlayerTurn()
            if(p_alive2==1):
                current_game = Game(4,Playerlist[1])
                Action = current_game.PlayerTurn()
            if(p_alive3==1):
                current_game = Game(4,Playerlist[2])
                Action = current_game.PlayerTurn()
            if(p_alive4==1):
                current_game = Game(4,Playerlist[3])
                Action = current_game.PlayerTurn()




        #for i in range(2):
        #    print(i)
        #    ewe = Game(4,Playerlist[i])
        #    action = ewe.PlayerTurn()
        
        
        #x=Playerlist[1].CurrentPlayer()

        #action = ewe.PlayerTurn()
        print(action)
        


ewe = Game(4,[])
ewe.startGame()
