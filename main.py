from game import Game
from player import Player
import random

def main():
    #Game.gameplay()
    #card1 = Card(5)
    #duke1 = Duke(1)
    #print(card1)
    #card1.cardprint()
    #duke1.cardprint()
    #j1 = Player(1,2,"uwu","awa")
    #j1.Getincome()
    #j1.SeeCoins()
    gaem = Game(4)
    gaem.startGame()
    j1 = Player(1,2,3,2)
    a = j1.DoCardAction()
    
    players = input("Añadir jugador en 1,2,3,4: ")
    x = players.split(",")
    random.shuffle(x)
    print(x[0])
    selec = input("Desafiar (1) , Challenge (2)")
    

if __name__=="__main__":
    main()