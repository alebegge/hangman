import os 
import random


class Hangman():
    """
    comments
    """

    def __init__(self):
        self.loop = True
        self.lives = 5
        self.correctly_guess = set()
        self.correctly_guess_word = []
        file_path = os.path.join(os.path.abspath(''), "words_list.txt")
        content_doc = open(f"{file_path}", "r", encoding='UTF-8').read()
        possible_words = [word for word in content_doc.splitlines() if len(word) >= 5]
        self.word_to_find = random.choice(possible_words).upper()
    
    def print_word(self):
        for x in self.word_to_find:
            if x in self.correctly_guess:
                self.correctly_guess_word.append(x)
            else:
                self.correctly_guess_word.append("_")
        print(" ".join(self.correctly_guess_word))
        self.correctly_guess_word = []

    def guess(self):
        self.letter = input("Please enter a letter or your guess: ").upper()
        if len(self.letter) == 1:
            if self.letter in self.word_to_find:
                print(f"Congratulation, {self.letter} is in the word!")
                self.correctly_guess.add(self.letter)
            else:
                self.lives -= 1
                print(f"Sorry, {self.letter} is not in the word! You lost a live.")
        else:
            if self.letter == self.word_to_find:
                print(f"Congratulation, {self.letter} was the right word!")
                self.lives = 0
            else:
                self.lives -= 1
                print(f"Sorry, {self.letter} is not the right word! You lost a live.")

    def replay(self):
        play_again = input("Would you like to play again ? (Y/N): ").upper()
        if play_again == "YES" or play_again == "Y":
            return "YES"
        else:
            return "NO"
