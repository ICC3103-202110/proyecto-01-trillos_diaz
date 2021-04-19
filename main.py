from game import Game
from card import Card
from duke import Duke
from player import Player

def main():
    #Game.gameplay()
    #card1 = Card(5)
    duke1 = Duke(1)
    #print(card1)
    #card1.cardprint()
    duke1.cardprint()
    j1 = Player(1,2,"uwu","awa")
    j1.Getincome()
    j1.SeeCoins()

if __name__=="__main__":
    main()