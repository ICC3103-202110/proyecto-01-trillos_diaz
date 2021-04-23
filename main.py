from game import Game
from player import Player
import random

def main():
    asking = 1
    while asking == 1:
        print("How many players do you want?")
        playaCount = int(input())
        if 3 <= playaCount <= 4:
            gaem = Game(playaCount)
            gaem.startGame()
            asking = 0
        else:
            print("Please input a valid number (3,4)")

    

if __name__=="__main__":
    main()