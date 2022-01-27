import os
import random


class Hangman():
    """
    This class object regroup all the functional method to play Hangman.
    We defining four methods used: print_word - guess - replay - exit.
    You need to call the class each time you want to play.  
    """

    def __init__(self):
        """ 
        lives = number of lives of the player.
        correctly_guess = set where the well guessed characters are stored.
        correctly_guess_word = is an empty list helping printing the hidden word.
        turn_count = the number of turn played by the player.
        word_to_find = the random word to be guessed by the player.
        """
        self.lives: int = 5
        self.correctly_guess: set = set()
        self.correctly_guess_word: list = []
        self.turn_count: int = 1
        file_path = os.path.join(os.path.abspath(''), "utils")
        file_path_final = os.path.join(f"{file_path}", "words_list.txt")
        content_doc = open(f"{file_path_final}", "r", encoding='UTF-8').read()
        possible_words = [
            word for word in content_doc.splitlines() if len(word) >= 5]
        self.word_to_find: str = random.choice(possible_words).upper()

    def print_word(self) -> None:
        """ 
        Short stockage memory restructuring the hidden word with the guesses
        and printing the word to find hidden. 
        """
        for x in self.word_to_find:
            if x in self.correctly_guess:
                self.correctly_guess_word.append(x)
            else:
                self.correctly_guess_word.append("_")
        print(" ".join(self.correctly_guess_word))
        self.correctly_guess_word = []

    def guess(self) -> None:
        """Asking the player to guess a number or a word."""
        print(f"########## TURN {self.turn_count} ##########")
        self.letter = input("Please enter a letter or your guess: ").upper()
        if len(self.letter) == 1:
            if self.letter in self.word_to_find:
                print(f"Congratulation, {self.letter} is in the word!\n")
                self.correctly_guess.add(self.letter)
            else:
                self.lives -= 1
                print(
                    f"Sorry, {self.letter} is not in the word! You lost a live.\n")
        else:
            if self.letter == self.word_to_find:
                print(f"Congratulation, {self.letter} was the right word!")
                print(f"You found it after {self.turn_count} turns. \n")
                self.lives = 0
            else:
                self.lives -= 1
                print(
                    f"Sorry, {self.letter} is not the right word! You lost a live.\n")
        self.turn_count += 1

    def replay(self) -> str:
        """Asking the player to play again. Return a str "YES" or "NO". """
        play_again = input("Would you like to play again ? (Y/N): ").upper()
        return play_again

    def exit(self) -> None:
        """ Printing an exit message. """
        print(f"We are sorry to hear that, have a nice day!")
