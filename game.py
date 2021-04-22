from deck import Deck
from player import Player
import random


class Game():
    def __init__(self,playerCount):
        self.playerCount = playerCount


    def DoCardAction(self,currPlaya,actTodo):
        if(actTodo==1):
            self.Playerlist[currPlaya-1].coinsChange(3)
            print("You got 3 coins from taxes!\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya-1].coins))
            return 1
            
        if(actTodo==2):
            print("What player do you want to attack?")
            AttackedPlaya =int(input())
            whatCards = [self.Playerlist[AttackedPlaya-1].specCardStatus(1),self.Playerlist[AttackedPlaya-1].specCardStatus(1)]
            if whatCards[0]== "hidden" and  whatCards[1]== "hidden":
                cardLost = random.randint(1,2)
                self.Playerlist[AttackedPlaya-1].cardStatusSet(cardLost)
                print("Player %d lost his influence card number %d"%(AttackedPlaya,cardLost))
            elif whatCards[0]== "hidden" and  whatCards[1]== "shown":
                self.Playerlist[AttackedPlaya-1].cardStatusSet(1)
                print("Player %d lost his influence card number 1"%(AttackedPlaya))
            elif whatCards[0]== "shown" and  whatCards[1]== "hidden":
                self.Playerlist[AttackedPlaya-1].cardStatusSet(2)
                print("Player %d lost his influence card number 2"%(AttackedPlaya))
            
            return 2
          
        if(actTodo==3):
            print("Your 2 cards")
            print("Pick which cards you want (a,b)")
            print(self.Playerlist[currPlaya-1].printCardType(1), " (1)")
            print(self.Playerlist[currPlaya-1].printCardType(2), " (2)")

            print("Top 2 cards in the deck")
            print(self.Ddeck.returnCardNo(0), " (3)")
            print(self.Ddeck.returnCardNo(1), " (4)")
            cardsWanted = input().split(",")
            if int(cardsWanted[0]) == 1 and int(cardsWanted[1]) == 2:
                print("You swap no cards cards")
                self.Playerlist[currPlaya-1].SeeCards()
            elif int(cardsWanted[0]) == 1 and int(cardsWanted[1]) == 3 and self.Playerlist[currPlaya-1].specCardStatus(2)== "hidden":
                
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,1),2)
                self.Playerlist[currPlaya-1].SeeCards()
            elif int(cardsWanted[0]) == 1 and int(cardsWanted[1]) == 4 and self.Playerlist[currPlaya-1].specCardStatus(2)== "hidden":
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,2),2)
                self.Playerlist[currPlaya-1].SeeCards()
            elif int(cardsWanted[0]) == 2 and int(cardsWanted[1]) == 3 and self.Playerlist[currPlaya-1].specCardStatus(1)== "hidden":
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
                self.Playerlist[currPlaya-1].SeeCards()
            elif int(cardsWanted[0]) == 2 and int(cardsWanted[1]) == 4 and self.Playerlist[currPlaya-1].specCardStatus(1)== "hidden":
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,2),1)
                self.Playerlist[currPlaya-1].SeeCards()
            elif int(cardsWanted[0]) == 3 and int(cardsWanted[1]) == 4:
                if self.Playerlist[currPlaya-1].specCardStatus(1)== "hidden" or self.Playerlist[currPlaya-1].specCardStatus(2)== "hidden":
                    print("You swap both cards")
                    self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
                    self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
                    self.Playerlist[currPlaya-1].SeeCards()
                else:
                    print("Please insert card numbers in order, or dont try to replace a shown card")
            else:
                print("Please insert card numbers in order, or dont try to replace a shown card")
            
            return 3
        if(actTodo==4):
            print("What player do you want to steal from?")
            AttackedPlaya =int(input())
            howManyCoins = self.Playerlist[AttackedPlaya-1].coins
            if howManyCoins >=2:
                print("You stole 2 coins from player %d\nYour current ammount of coins is %d"%(AttackedPlaya,self.Playerlist[currPlaya-1].coins))
                print("Player %d has %d coins left!"%(AttackedPlaya,self.Playerlist[currPlaya-1].coins))
            elif howManyCoins == 1:
                print("Player %d has only 1 coin"%(AttackedPlaya))
                print("You stole 1 coin from him\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya-1].coins))
                print("Player %d has no coins left!")
            elif howManyCoins == 0:
                print("Player %d did´t have any coins left!"%(AttackedPlaya))
                print("So you wasted your turn and did not gain anything\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya-1].coins))
                
            return 4


    def counterAction(self,currPlaya):
        counterPlayers = []
        
        print("Does any player want to respond to this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
        counterPlayers = input().split(",")
        print(counterPlayers)
        if counterPlayers[0]=="":
            return 1
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
                    print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                    counterPlayers = input().split(",")
                    print("h")
                    print(counterPlayers)
                    print("a")
                    if counterPlayers[0]=="":
                        print("e")
                        return 0
                    elif self.playerCount > len(counterPlayers) >= 2:
                        print("ewe")
                        print("picking random player from the players that decided to attack")
                        random.shuffle(counterPlayers)
                        playerchallenge = int(counterPlayers[0])
                        if playerchallenge == currPlaya:
                            print("bruh3")
                        else:
                            print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                            self.canDoAction = self.challengePlayer(playerattack,playerchallenge)
                            return self.canDoAction
                    elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                        print("uwu")
                        playerchallenge = int(counterPlayers[0])
                        if playerchallenge == currPlaya:
                            print("bruh3")
                        else:
                            print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                            self.canDoAction = self.challengePlayer(playerattack,playerchallenge)
                            return self.canDoAction
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
                    print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                    counterPlayers = input().split(",")
                    print(counterPlayers)
                    print("hdjashdj")
                    if counterPlayers[0]=="":
                        return 0
                    elif self.playerCount > len(counterPlayers) >= 2:
                        print("picking random player from the players that decided to attack")
                        random.shuffle(counterPlayers)
                        playerchallenge = int(counterPlayers[0])
                        if playerattack == currPlaya:
                            print("bruh3")
                        else:
                            print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                            self.canDoAction = self.challengePlayer(playerattack,playerchallenge)
                            return self.canDoAction
                            
                
                        ###uwu awa seguir aca
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
            print("The challenged player %d was not bluffing!!"%(currPlaya))
            #self.Playerlist[currPlaya-1].SeeCards()
            #print(self.Ddeck.returnDeck())
            self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
            cardLost = random.randint(1,2)
            #print(self.Ddeck.returnDeck())
            #self.Playerlist[currPlaya-1].SeeCards()
            print("So player %d lost his influence card number %d"%(playerattack,cardLost))
            self.Playerlist[playerattack-1].cardStatusSet(cardLost)
            return 1
        elif(whatItDo[1]==self.currActionPlaying and self.Playerlist[currPlaya-1].specCardStatus(2)=="hidden"):
            print("The challenged player %d was not bluffing!!"%(currPlaya))
            #self.Playerlist[currPlaya-1].SeeCards()
            #print(self.Ddeck.returnDeck())
            self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,1),2)
            cardLost = random.randint(1,2)
            #print(self.Ddeck.returnDeck())
            #self.Playerlist[currPlaya-1].SeeCards()
            print("So player %d lost his influence card number %d"%(playerattack,cardLost))
            self.Playerlist[playerattack-1].cardStatusSet(cardLost)
            return 1
        else:
            print("The challenged player %d was bluffing!!"%(currPlaya))
            #print(self.Playerlist[currPlaya-1].specCardStatus(1))
            #print(self.Playerlist[currPlaya-1].specCardStatus(2))
            cardLost = random.randint(1,2)
            self.Playerlist[currPlaya-1].cardStatusSet(cardLost)
            print("So he looses his influence card number %d"%(cardLost))
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
                    self.DoCardAction(playy,1)
                else:
                    print("No hace la accion")
                return 1
                
            if(select==2):
                self.currActionPlaying = 2
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                    self.DoCardAction(playy,2)
                else:
                    print("No hace la accion")
                return 2
            
            if(select==3):
                self.currActionPlaying = 1
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                    self.DoCardAction(playy,3)
                else:
                    print("No hace la accion")
                return 3
            if(select==4):
                self.currActionPlaying = 3
                self.canDoAction = self.counterAction(playy)
                if self.canDoAction ==1:
                    print("Hace la accion")
                    self.DoCardAction(playy,4)
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
