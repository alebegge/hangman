from ast import Break
import os 
import pandas as pd 
import numpy as np 
from collections import Counter

from utils.game import *


print('Welcome to the Hangman Game')
print("Ok, let's go !")
playing = Hangman()

loop = 1
while loop > 0:
    playing.show_word()
    while playing.lives > 0:
        print(f'You have now {playing.lives} lives left to guess the word.')
        playing.guess()
    
    else:
        print(f"We are sorry but you lost !")
        play_again = input("Would you like to play again ? (Y/N)").upper()
        
        if play_again == "yes" or "y":
            playing = Hangman()
            loop = 1
        else:
            print("Thanks for playing, see you soon!")
            loop = -1

            










