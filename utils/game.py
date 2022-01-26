import os 
from collections import Counter
import random


class Hangman():
    """
    comments
    """

    def __init__(self):
        self.lives = 5
        self.correctly_guess = []
        file_path = os.path.join(os.path.abspath(''), "words_list.txt")
        content_doc = open(f"{file_path}", "r", encoding='UTF-8').read()
        self.possible_words = [word for word in content_doc.splitlines() if len(word) >= 5]
        self.word_to_find = random.choice(self.possible_words).upper()
    
    def show_word(self):
        self.hidden_word = ["_" for x in self.word_to_find]
        # print(self.word_to_find)
        print(" ".join(self.hidden_word))

    def guess(self):
        self.letter = input("Please enter a letter or your guess:").upper()
        if len(self.letter) == 1:
            if self.letter in self.word_to_find:
                print(f"Congratulation, {self.letter} is in the word!")
                self.correctly_guess.append(self.letter)
                for elem in self.correctly_guess:
                    self.hidden_word = [elem if elem == char else "_" for char in self.word_to_find]
                print(self.hidden_word)
            else:
                self.lives -= 1
                print(f"Sorry, {self.letter} is not in the word. You lost a live. You have now {self.lives}!")
        else:
            self.word_guess()
    
    def word_guess(self):
        if self.letter == self.word_to_find:
            print(f"Congratulation, {self.letter} was the right word!")
        else:
            self.lives -= 1
            print(f'Sorry, {self.letter} is not the word we are looking for. You have now {self.lives}')
