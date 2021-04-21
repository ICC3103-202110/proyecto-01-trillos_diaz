from deck import Deck
from player import Player
import random


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
    def counterAction(self,currPlaya):
        counterPlayers = []
        
        print("Does any player want to respond to this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
        counterPlayers = input().split(",")
        print(counterPlayers)
        if counterPlayers[0]=="":
            return 0
        elif self.playerCount > len(counterPlayers) >= 2:
            print("picking random player from the players that decided to attack")
            random.shuffle(counterPlayers)
            playerattack = int(counterPlayers[0])
            if playerattack == currPlaya:
                print("bruh2")
            else:
                print("Player %d was chosen to do an action"%(playerattack))
                print("Player %d, what do you wish to do?\nCOUNTERATTACK = (0)\nCHALLENGE =(1)"%(playerattack))
                whattodo = int(input())
                if whattodo == 0:
                    print("Player %d counterattacks Player %d!!"%(playerattack,currPlaya))
                    ##
                elif whattodo == 1:
                    print("Player %d challenges Player %d!!"%(playerattack,currPlaya))
                    self.canDoAction = self.challengePlayer(currPlaya,playerattack)
                    return self.canDoAction
        elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
            playerattack = int(counterPlayers[0])
            if playerattack == currPlaya:
                print("bruh2")
            else:
                print("Player %d chose to do an action"%(playerattack))
                print("Player %d, what do you wish to do?\nCOUNTERATTACK = (0)\nCHALLENGE =(1)"%(playerattack))
                whattodo = int(input())
                if whattodo == 0:
                    print("Player %d counterattacks Player %d!!"%(playerattack,currPlaya))
                elif whattodo == 1:
                    print("Player %d challenges Player %d!!"%(playerattack,currPlaya))
                    self.canDoAction = self.challengePlayer(currPlaya,playerattack)
                    return self.canDoAction
        else:
            print("bruh1")
            

    def challengePlayer(self,currPlaya,playerattack):
        print(currPlaya)
        
        print(self.Playerlist[currPlaya-1].canDoRial())
        whatItDo = self.Playerlist[currPlaya-1].canDoRial()
        print(whatItDo)
        if( whatItDo[0]==self.currActionPlaying and self.Playerlist[currPlaya-1].specCardStatus(1)=="hidden"):
            print("La primera carta de este jugador permite hacer la accion")
            #self.Playerlist[currPlaya-1].SeeCards()
            #print(self.Ddeck.returnDeck())
            self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1),1)
            #print(self.Ddeck.returnDeck())
            #self.Playerlist[currPlaya-1].SeeCards()
            self.Playerlist[playerattack].cardStatusSet(random.randint(0,2))
            return 1
        elif(whatItDo[1]==self.currActionPlaying and self.Playerlist[currPlaya-1].specCardStatus(2)=="hidden"):
            print("La segunda carta de este jugador permite hacer la accion")
            #self.Playerlist[currPlaya-1].SeeCards()
            #print(self.Ddeck.returnDeck())
            self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2),2)
            #print(self.Ddeck.returnDeck())
            #self.Playerlist[currPlaya-1].SeeCards()
            self.Playerlist[playerattack].cardStatusSet(random.randint(0,2))
            return 1
        else:
            print("El jugador desafiado estaba bluffeando!!")
            #print(self.Playerlist[currPlaya-1].specCardStatus(1))
            #print(self.Playerlist[currPlaya-1].specCardStatus(2))
            self.Playerlist[currPlaya-1].cardStatusSet(random.randint(0,2))
            #print(self.Playerlist[currPlaya-1].specCardStatus(1))
            #print(self.Playerlist[currPlaya-1].specCardStatus(2))
            return 0
    
    def PlayerTurn(self,currPlaya):
        playy = currPlaya+1
        self.canDoAction = 1
        print("Player number %d it's your turn"%(playy))
        print("Player %d do you want to perform a Normal accion(Coin draw) or a card accion"%(playy))
        print("CARD ACTION = (0)\nNORMAL ACTION = (1)")
        select =int(input())
        if(select==0):
            print("\nPlease select wich Card Action you want to perform")
            print("TAX = (1)\nASSASSINATE = (2)\nEXCHANGE = (3)\nSTEAL = (4)\n")
            select = int(input())
            if(select==1):
                self.currActionPlaying = 5
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                else:
                    print("No hace la accion")
                return 1
                
            if(select==2):
                self.currActionPlaying = 2
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                else:
                    print("No hace la accion")
                return 2
            
            if(select==3):
                self.currActionPlaying = 1
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                else:
                    print("No hace la accion")
                return 3
            if(select==4):
                self.currActionPlaying = 3
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                else:
                    print("No hace la accion")
                return 4
        elif(select==1):
            print("Please Select wich Normal Action you want to perform")
            print("INCOME= (1)\n2:FOREING AID= (2)\n3:COUP = (3)")
            select = int(input())
            #if(select==1):
            

    def startGame(self):
        #start
        self.Ddeck = Deck()
        self.Ddeck.GenerateCards()
        print(self.Ddeck)
        self.Playerlist=[]
        card11 = self.Ddeck.takeCard()
        card22 = self.Ddeck.takeCard()
        player1 = Player(1,2,card11,card22)
        #player1.SeeCards()
        #print(player1.canDoRial())
        self.Playerlist.append(player1)
        card11 = self.Ddeck.takeCard()
        card22 = self.Ddeck.takeCard()
        player2 = Player(2,2,card11,card22)
        #player2.SeeCards()
        self.Playerlist.append(player2)
        card11 = self.Ddeck.takeCard()
        card22 = self.Ddeck.takeCard()
        player3 = Player(3,2,card11,card22)
        self.Playerlist.append(player3)
        #player3.SeeCards()
        if self.playerCount == 4:
            card11 = self.Ddeck.takeCard()
            card22 = self.Ddeck.takeCard()
            player4 = Player(4,2,card11,card22)
            self.Playerlist.append(player4)
            #player4.SeeCards()
        print("bruh")
        #player1.SeeCoins()
        #player1.coins()
        #player1.SeeCoins()
        #player1.canDoRial()
        #player1.cardCoinCost(1)
        #print(player1.gameStatus())
        ActiveGame = 1
        curPlaya = 1
        print(self.Playerlist[curPlaya-1].isInGame)
        while(ActiveGame==1):
            #print("a")
            if(self.Playerlist[curPlaya-1].isInGame==1):
                print("a")
                Action = self.PlayerTurn(curPlaya-1)
                ActiveGame = 0
            else:
                print("fucc")
                ActiveGame = 0





        #for i in range(2):
        #    print(i)
        #    ewe = Game(4,Playerlist[i])
        #    action = ewe.PlayerTurn()
        
        
        #x=Playerlist[1].CurrentPlayer()

        #action = ewe.PlayerTurn()
        print(Action)
        


#ewe = Game(4,[])
#ewe.startGame()
