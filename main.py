import time

from utils.game import *


print('Welcome to the Hangman Game')
print("Ok, let's go !")
general_loop = input("Are you ready to play ? (Y/N): ").upper()

while general_loop == "Y" or general_loop == "YES":

    playing = Hangman()
    print(f"Our system is picking a random number for you....")
    time.sleep(2)
    print(f"The word to be guess is: ")

    while playing.lives > 0:
        playing.print_word()
        print('')
        playing.guess()
        if playing.lives > 0:
            print(f"You have now {playing.lives} lives left.\n")
    else:
        general_loop = playing.replay()

else:
    playing.exit()
