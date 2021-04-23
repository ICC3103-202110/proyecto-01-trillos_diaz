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
            whatCards = [self.Playerlist[AttackedPlaya-1].specCardStatus(1),self.Playerlist[AttackedPlaya-1].specCardStatus(2)]
            print(whatCards)
            if whatCards[0]== "hidden" and  whatCards[1]== "hidden":
                cardLost = random.randint(1,2)
                self.Playerlist[AttackedPlaya-1].cardStatusSet(cardLost)
                print("Player %d lost his influence card number %d"%(AttackedPlaya,cardLost))
                self.Playerlist[AttackedPlaya-1].gameStatus()
                print(whatCards)
            elif whatCards[0]== "hidden" and  whatCards[1]== "shown":
                self.Playerlist[AttackedPlaya-1].cardStatusSet(1)
                print("Player %d lost his influence card number 1"%(AttackedPlaya))
                self.Playerlist[AttackedPlaya-1].gameStatus()
            elif whatCards[0]== "shown" and  whatCards[1]== "hidden":
                self.Playerlist[AttackedPlaya-1].cardStatusSet(2)
                print("Player %d lost his influence card number 2"%(AttackedPlaya))
                self.Playerlist[AttackedPlaya-1].gameStatus()
            
            return 2
          
        if(actTodo==3):
            print("Pick which cards you want (a,b)")
            print("Your 2 cards")
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
                    self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,1),2)
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
                self.Playerlist[currPlaya-1].coinsChange(2)
                print("You stole 2 coins from player %d\nYour current ammount of coins is %d"%(AttackedPlaya,self.Playerlist[currPlaya-1].coins))
                self.Playerlist[AttackedPlaya-1].coinsChange(-2)
                print("Player %d has %d coins left!"%(AttackedPlaya,self.Playerlist[AttackedPlaya-1].coins))
            elif howManyCoins == 1:
                print("Player %d has only 1 coin"%(AttackedPlaya))
                self.Playerlist[currPlaya-1].coinsChange(1)
                print("You stole 1 coin from him\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya-1].coins))
                self.Playerlist[AttackedPlaya-1].coinsChange(-1)
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
                playerattack = int(counterPlayers[1])
            elif self.Playerlist[playerattack-1].isInGame == 0:
                return 1
            print("Player %d was chosen to do an action"%(playerattack))
            print("Player %d, what do you wish to do?\nCOUNTERATTACK = (0)\nCHALLENGE =(1)"%(playerattack))
            whattodo = int(input())
            if whattodo == 0:
                print("Player %d counterattacks Player %d!!"%(playerattack,currPlaya))
                print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                counterPlayers = input().split(",")
                print(counterPlayers)
                if counterPlayers[0]=="":
                    return 0
                elif self.playerCount > len(counterPlayers) >= 2:
                    print("picking random player from the players that decided to attack")
                    random.shuffle(counterPlayers)
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        playerchallenge = int(counterPlayers[1])
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        return 0
                    print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))  
                    self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                    return self.canDoAction
                elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                    #print("uwu")
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        return 0
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        return 0
                    else:
                        print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                        self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                        return self.canDoAction
            elif whattodo == 1:
                print("Player %d challenges Player %d!!"%(playerattack,currPlaya))
                self.canDoAction = self.challengePlayer(currPlaya,playerattack,1)
                return self.canDoAction
        elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
            playerattack = int(counterPlayers[0])
            if playerattack == currPlaya:
                return 0
            elif self.Playerlist[playerattack-1].isInGame == 0:
                return 1
            else:
                print("Player %d chose to do an action"%(playerattack))
                print("Player %d, what do you wish to do?\nCOUNTERATTACK = (0)\nCHALLENGE =(1)"%(playerattack))
                whattodo = int(input())
                if whattodo == 0:
                    print("Player %d counterattacks Player %d!!"%(playerattack,currPlaya))
                    print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                    counterPlayers = input().split(",")
                    print(counterPlayers)
                    if counterPlayers[0]=="":
                        return 0
                    elif self.Playerlist[counterPlayers-1].isInGame == 0:
                        return 0
                    elif self.playerCount > len(counterPlayers) >= 2:
                        print("picking random player from the players that decided to attack")
                        random.shuffle(counterPlayers)
                        playerchallenge = int(counterPlayers[0])
                        if playerchallenge == currPlaya:
                            playerchallenge = int(counterPlayers[1])
                        print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                        self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                        return self.canDoAction
                            
                elif whattodo == 1:
                    print("Player %d challenges Player %d!!"%(playerattack,currPlaya))
                    self.canDoAction = self.challengePlayer(currPlaya,playerattack,1)
                    return self.canDoAction
        else:
            print("bruh1")
            

    def challengePlayer(self,currPlaya,playerattack,mode):
        print(currPlaya)
        actionToChall = self.currActionPlaying    
        print(self.Playerlist[currPlaya-1].canDoRial())
        whatItDo = self.Playerlist[currPlaya-1].canDoRial()
        print(whatItDo)
        if mode == 1:
            if( whatItDo[0]==actionToChall and self.Playerlist[currPlaya-1].specCardStatus(1)=="hidden"):
                print("The challenged player %d was not bluffing!!"%(currPlaya))
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
                cardLost = random.randint(1,2)
                print("So player %d lost his influence card number %d"%(playerattack,cardLost))
                self.Playerlist[playerattack-1].cardStatusSet(cardLost)
                self.Playerlist[playerattack-1].gameStatus()
                return 1
            elif(whatItDo[1]==actionToChall and self.Playerlist[currPlaya-1].specCardStatus(2)=="hidden"):
                print("The challenged player %d was not bluffing!!"%(currPlaya))
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,1),2)
                cardLost = random.randint(1,2)
                print("So player %d lost his influence card number %d"%(playerattack,cardLost))
                self.Playerlist[playerattack-1].cardStatusSet(cardLost)
                self.Playerlist[playerattack-1].gameStatus()
                return 1
            else:
                print("The challenged player %d was bluffing!!"%(currPlaya))
                cardLost = random.randint(1,2)
                self.Playerlist[currPlaya-1].cardStatusSet(cardLost)
                print("So he loses his influence card number %d"%(cardLost))
                self.Playerlist[currPlaya-1].gameStatus()
                return 0
        elif mode == 2:
            
            print(self.Playerlist[currPlaya-1].printCardType(1))
            print(self.Playerlist[currPlaya-1].printCardType(2))
            if actionToChall ==2:
                actionToChall = 4
            elif actionToChall ==3:
                actionToChall = 13
            elif actionToChall == 6:
                actionToChall = 5
            else:
                return 1
                
            actiontoChallS = str(actionToChall)
            print(actiontoChallS)
            print(str(whatItDo[0]))
            print(str(whatItDo[1]))
            if actiontoChallS.find( str(whatItDo[0])) != -1 and self.Playerlist[currPlaya-1].specCardStatus(1)=="hidden":
                print("estaweafunciona1")
                print("The challenged player %d was not bluffing!!"%(currPlaya))
                
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card1,1),1)
                cardLost = random.randint(1,2)
                print("So player %d lost his influence card number %d"%(playerattack,cardLost))
                print(self.Playerlist[currPlaya-1].printCardType(1))
                print(self.Playerlist[currPlaya-1].printCardType(2))
                self.Playerlist[playerattack-1].cardStatusSet(cardLost)
                self.Playerlist[playerattack-1].gameStatus()
                return 1
            elif actiontoChallS.find( str(whatItDo[1])) != -1 and self.Playerlist[currPlaya-1].specCardStatus(1)=="hidden":
                print("estaweafunciona2")
                print("The challenged player %d was not bluffing!!"%(currPlaya))
                self.Playerlist[currPlaya-1].setCard(self.Ddeck.replaceCard(self.Playerlist[currPlaya-1].card2,1),2)
                cardLost = random.randint(1,2)
                print("So player %d lost his influence card number %d"%(playerattack,cardLost))
                print(self.Playerlist[currPlaya-1].printCardType(1))
                print(self.Playerlist[currPlaya-1].printCardType(2))
                self.Playerlist[playerattack-1].cardStatusSet(cardLost)
                self.Playerlist[playerattack-1].gameStatus()
                return 1
            else:
                print("estaweafunciona3")
                print("The challenged player %d was bluffing!!"%(currPlaya))
                cardLost = random.randint(1,2)
                self.Playerlist[currPlaya-1].cardStatusSet(cardLost)
                print("So he looses his influence card number %d"%(cardLost))
                self.Playerlist[currPlaya-1].gameStatus()
                print(self.Playerlist[currPlaya-1].printCardType(1))
                print(self.Playerlist[currPlaya-1].printCardType(2))
                return 0
            
    
    def PlayerTurn(self,currPlaya):
        playy = currPlaya+1
        self.canDoAction = 1
        print("Player number %d it's your turn"%(playy))
        ccoins = 0
        while ccoins < self.playerCount:
            print("Player %d´s coins: %d"%(ccoins+1,self.Playerlist[ccoins].coins))
            ccoins +=1
        print("Your cards:        %s , %s"%(self.Playerlist[currPlaya].printCardType(1),self.Playerlist[currPlaya].printCardType(2)))
        print("Your cards status: %s , %s"%(self.Playerlist[currPlaya].specCardStatus(1),self.Playerlist[currPlaya].specCardStatus(2)))
        if self.Playerlist[currPlaya].coins >= 10:
            print("You automatically do a coup!")
            print("What player do you want to do a coup on?")
            loop = 0
            while loop == 0:
                playerToCoup = int(input())
                if(playerToCoup==playy or playerToCoup<0 or playerToCoup>len(self.Playerlist)):
                    loop = 0
                    print("You can't select that, Select again")
                elif(playerToCoup<0 and playerToCoup>len(self.Playerlist)):
                    loop = 1
            cardLost = random.randint(1,2)
            print("So player %d lost his influence card number %d"%(playerToCoup,cardLost))
            self.Playerlist[playerToCoup-1].cardStatusSet(cardLost)
            self.Playerlist[playerToCoup-1].gameStatus()
            self.Playerlist[currPlaya].coinsChange(-7)
            print("Your current ammount of coins is %d"%(self.Playerlist[currPlaya].coins))
            return 6
        print("Player %d do you want to perform a Normal accion(Coin draw) or a card accion"%(playy))
        print("CARD ACTION = (0)\nNORMAL ACTION = (1)")
        select =int(input())
        if(select==0):
            print("\nPlease select wich Card Action you want to perform")
            print("TAX = (1)\nASSASSINATE = (2)\nEXCHANGE = (3)\nSTEAL = (4)\n")
            select = int(input())
            if(select==1):
                self.currActionPlaying = 5
                print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                counterPlayers = input().split(",")
                print(counterPlayers)
                if counterPlayers[0]=="":
                    self.canDoAction == 1
                elif self.playerCount > len(counterPlayers) >= 2:
                    print("picking random player from the players that decided to attack")
                    random.shuffle(counterPlayers)
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        playerchallenge = int(counterPlayers[1])
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        self.canDoAction = 0
                    else:
                        print("Player %d challenges Player %d!!"%(playerchallenge,playy))
                        self.canDoAction = self.challengePlayer(playy,playerchallenge,1)
                elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        self.canDoAction = 0
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        self.canDoAction = 0
                    else:
                        print("Player %d challenges Player %d!!"%(playerchallenge,playy))
                        self.canDoAction = self.challengePlayer(playy,playerchallenge,1)
                        #return self.canDoAction
                if self.canDoAction ==1:
                    print("You manage to do the action")
                    self.DoCardAction(playy,1)
                else:
                    print("No hace la accion")
                return 1
                
            if(select==2):
                if self.Playerlist[currPlaya].coins >= 3:
                    self.currActionPlaying = 2
                    self.canDoAction = self.counterAction(playy)
                    if self.canDoAction ==1:
                        print("You manage to do the action")
                        self.DoCardAction(playy,2)
                        self.Playerlist[currPlaya].coinsChange(-3)
                        print("Your current ammount of coins is %d"%(self.Playerlist[currPlaya].coins))
                    else:
                        print("No hace la accion")
                    return 2
                else:
                    print("You don´t have enough coins to do this action")
            
            if(select==3):
                self.currActionPlaying = 1
                print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                counterPlayers = input().split(",")
                print(counterPlayers)
                if counterPlayers[0]=="":
                    self.canDoAction == 1
                elif self.playerCount > len(counterPlayers) >= 2:
                    print("picking random player from the players that decided to attack")
                    random.shuffle(counterPlayers)
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        playerchallenge = int(counterPlayers[1])
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        self.canDoAction = 0
                    else:
                        print("Player %d challenges Player %d!!"%(playerchallenge,playy))
                        self.canDoAction = self.challengePlayer(playy,playerchallenge,1)
                elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                    playerchallenge = int(counterPlayers[0])
                    if playerchallenge == currPlaya:
                        self.canDoAction = 0
                    elif self.Playerlist[playerchallenge-1].isInGame == 0:
                        self.canDoAction = 0
                    else:
                        print("Player %d challenges Player %d!!"%(playerchallenge,playy))
                        self.canDoAction = self.challengePlayer(playy,playerchallenge,1)
                        #return self.canDoAction
                if self.canDoAction ==1:
                    print("You manage to do the action")
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
            print("1:INCOME= (1)\n2:FOREING AID= (2)\n3:COUP = (3)")
            select = int(input())
            if select==1:
                self.Playerlist[currPlaya].coinsChange(1)
                print("You got 1 coins from income!\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya-1].coins))
                return 5
            elif select == 2:
                self.currActionPlaying = 6
                print("Does any player want to Counterattack this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                counterPlayers = input().split(",")
                print(counterPlayers)
                if counterPlayers[0]=="":
                    self.canDoAction == 1
                elif self.playerCount > len(counterPlayers) >= 2:
                    print("picking random player from the players that decided to attack")
                    random.shuffle(counterPlayers)
                    playerattack = int(counterPlayers[0])
                    if playerattack == currPlaya:
                        playerattack = int(counterPlayers[1])
                    elif self.Playerlist[playerattack-1].isInGame == 0:
                        self.canDoAction = 1
                    else:
                        print("Player %d CounterAttack Player %d"%(playerattack,currPlaya+1))
                        print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                        counterPlayers = input().split(",")
                        print(counterPlayers)
                        if counterPlayers[0]=="":
                            self.canDoAction == 1
                        elif self.playerCount > len(counterPlayers) >= 2:
                            print("picking random player from the players that decided to attack")
                            random.shuffle(counterPlayers)
                            playerchallenge = int(counterPlayers[0])
                            if playerchallenge == currPlaya:
                                playerchallenge = int(counterPlayers[1])
                            elif self.Playerlist[playerchallenge-1].isInGame == 0:
                                self.canDoAction = 0
                            else:
                                print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                                self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                        elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                            playerchallenge = int(counterPlayers[0])
                            if playerchallenge == currPlaya:
                                self.canDoAction = 0
                            elif self.Playerlist[playerchallenge-1].isInGame == 0:
                                self.canDoAction = 0
                            else:
                                print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                                self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                                #return self.canDoAction
                elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :

                    playerattack = int(counterPlayers[0])
                    if playerattack == currPlaya:
                        playerattack = int(counterPlayers[1])
                    elif self.Playerlist[playerattack-1].isInGame == 0:
                        self.canDoAction = 1
                    else:
                        print("Player %d CounterAttack Player %d"%(playerattack,currPlaya+1))
                        print("Does any player want to Challenge this action?\nIf more than one, use separate player numbers by using commas\nor leave empty if no one wants to do anything")
                        counterPlayers = input().split(",")
                        print(counterPlayers)
                        if counterPlayers[0]=="":
                            self.canDoAction == 1
                        elif self.playerCount > len(counterPlayers) >= 2:
                            print("picking random player from the players that decided to attack")
                            random.shuffle(counterPlayers)
                            playerchallenge = int(counterPlayers[0])
                            if playerchallenge == currPlaya:
                                playerchallenge = int(counterPlayers[1])
                            elif self.Playerlist[playerchallenge-1].isInGame == 0:
                                self.canDoAction = 0
                            else:
                                print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                                self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)
                        elif len(counterPlayers) == 1 and len(counterPlayers) <= self.playerCount :
                            playerchallenge = int(counterPlayers[0])
                            if playerchallenge == currPlaya:
                                self.canDoAction = 0
                            elif self.Playerlist[playerchallenge-1].isInGame == 0:
                                self.canDoAction = 0
                            else:
                                print("Player %d challenges Player %d!!"%(playerchallenge,playerattack))
                                self.canDoAction = self.challengePlayer(playerattack,playerchallenge,2)


                    #playerattack = int(counterPlayers[0])
                    #if playerattack == currPlaya:
                    #   self.canDoAction = 1
                    #elif self.Playerlist[playerchallenge-1].isInGame == 0:
                    #    self.canDoAction = 1
                    #else:
                    #    print("Player %d challenges Player %d!!"%(playerchallenge,currPlaya+1))
                    #    self.canDoAction = self.challengePlayer(currPlaya,playerchallenge,2)
                    #    return self.canDoAction

                if self.canDoAction ==1:
                    print("Hace la accion")
                    self.Playerlist[currPlaya].coinsChange(2)
                    print("You got 2 coins from from a foreing country!\nYour current ammount of coins is %d"%(self.Playerlist[currPlaya].coins))
                else:
                    print("No hace la accion")
                return 6


            elif select == 3:
                if self.Playerlist[currPlaya].coins >= 7:
                    print("What player do you want to do a coup on?")
                    playerToCoup = int(input())
                    cardLost = random.randint(1,2)
                    print("So player %d lost his influence card number %d"%(playerToCoup,cardLost))
                    self.Playerlist[playerToCoup-1].cardStatusSet(cardLost)
                    self.Playerlist[playerToCoup-1].gameStatus()
                    self.Playerlist[currPlaya].coinsChange(-7)
                    print("Your current ammount of coins is %d"%(self.Playerlist[currPlaya].coins))
                    return 6
                else:
                    print("You don´t have enough coins to do this action")

    def savelog(self,action):
        self.Log.append(action)

    def printlog(self):
        for i in range(len(self.Log)):
            print(self.Log[i])       

    def startGame(self):
        #start
        self.Log=[]
        #self.savelog("ewe")
        #self.savelog("fgfg")
        print("aaa")
        #self.printlog()
        self.Ddeck = Deck()
        self.Ddeck.GenerateCards()
        #print(self.Ddeck)
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
        #print("bruh")
        #player1.SeeCoins()
        #player1.coins()
        #player1.SeeCoins()
        #player1.canDoRial()
        #player1.cardCoinCost(1)
        #print(player1.gameStatus())
        ActiveGame = 1
        curPlaya = 1
        turnNum = 1
        #print(self.Playerlist[curPlaya-1].isInGame)
        print(len(self.Playerlist))
        while(ActiveGame==1):
            #print("a")
            if(self.Playerlist[curPlaya-1].isInGame==1):

                print("Turn number %d\n"%(turnNum))
                self.PlayerTurn(curPlaya-1)
                curPlaya+=1
                if curPlaya>self.playerCount:
                    curPlaya = 1
                    turnNum+=1
                

            else:
                curPlaya+=1
                if curPlaya>self.playerCount:
                    curPlaya = 1
                    turnNum+=1





