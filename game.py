#==============================================#
# imports                                      #
#==============================================#

import sys
import os
import random
import time


#==============================================#
# vars                                         #
#==============================================#

p1s = 0
p2s = 0
goal = 3


#==============================================#
# functions                                    #
#==============================================#

# defines the game logic
def logic(p1, p2):
    global p1s, p2s
    # checks if the input is valid or not
    if not ((p1 == "1" or p1 == "2" or p1 == "3") and (p2 == "1" or p2 == "2" or p2 == "3")):
        print("something went wrong")
        main()
    else:
        # compares players moves and decides who is the winner
        if p1 == p2:
            print("that's a tie ...")
            time.sleep(1)

        if p1 == "1":
            if p2 == "2":
                print("player2 wins!!")
                p2s += 1
                time.sleep(1)
            elif p2 == "3":
                print("player1 wins!!")
                p1s += 1
                time.sleep(1)

        if p1 == "2":
            if p2 == "1":
                print("player1 wins!!")
                p1s += 1
                time.sleep(1)
            elif p2 == "3":
                print("player2 wins!!")
                p2s += 1
                time.sleep(1)

        if p1 == "3":
            if p2 == "1":
                print("player2 wins!!")
                p2s += 1
                time.sleep(1)
            elif p2 == "2":
                print("player1 wins!!")
                p1s += 1
                time.sleep(1)


# deletes the previous line
def deleteLine():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


# asks for play again or exit
def exit():
    global p1s, p2s, goal
    playAgain = input(" \ndo you want to play again ? y/n   ")
    if playAgain == "y":
        p1s = 0
        p2s = 0
        goal = 3
        header()
        # asks for game mode
        gameMode = input("multiplayer or single player? m/s   ").lower()
        deleteLine()
        while p1s != goal and p2s != goal:
            header()
            main()
        else:
            header()
            print("We have a WINNER!!!")
            exit()
    elif playAgain == "n":
        sys.exit()
    else:
        exit()


# main function
def main():
    global p1s, p2s, goal, gameMode

    #==============================#
    # MULTI PLAYER                 #
    #==============================#

    if gameMode == "m":
        # gets palyers moves
        player1 = input("player 1 choose your move number:  ").lower()
        deleteLine()
        player2 = input("player 2 choose your move number:  ").lower()
        deleteLine()
        logic(player1, player2)

    #==============================#
    # SINGLE PLAYER                #
    #==============================#

    elif gameMode == "s":
        # gets palyers moves
        player1 = input("player 1 choose your move number:  ").lower()
        deleteLine()
        player2 = str(random.randint(1, 3))
        print(f"Computer move was: {player2}")
        logic(player1, player2)

    else:
        os.system('cls')
        main()

    #==============================#
    # Bazi be 2                    #
    #==============================#

    if p1s == goal - 1 and p2s == goal - 1:
        goal += 1


# prints banner and scoreboard
def header():
    # clears everything before program's start
    os.system('cls')

    print(f"""
    ###################                      +---------------+
    ##               ##                      |               |
    ##  1. rock      ##                      |  player1   {p1s}  |
    ##  2. paper     ##                      |               |
    ##  3. scissors  ##                      |  player2   {p2s}  |
    ##               ##                      |               |
    ###################                      +---------------+
    """)


#==============================================#
# func calls and stuff                         #
#==============================================#

header()

# asks for game mode
gameMode = input("multiplayer or single player? m/s   ").lower()
deleteLine()

# runs the program
while p1s != goal and p2s != goal:
    header()
    main()
else:
    header()
    print("We have a WINNER!!!")
    exit()


#==============================================#
#                     TODO                     #
#==============================================#

# vaghti bazi reload mishe input gamemode dg taasiri nadare va bahamoon ghabli edame peyda mikone
# emtehane halat haye eshtebah vared shodane gozine ha
# func kardane ghesmate func and stuff va farakhani an dar exit()
