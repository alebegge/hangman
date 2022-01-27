# Hangman

Hangman is a playing game where you have to guess a random word by picking letters. 

![Hangman (Image)](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRUHTIeLzURMGGPk6nHZrUeqMQtR9FUrqfFCQ&usqp=CAU)


This is a basic version of the game and doesn't hold a graphical interface. 

## Installation

The files should be displayed as follow: 
```bash

└───hangman
    │   main.py
    │   README.md
    │
    └───utils
            game.py
            words_list.txt

```
- `Game.py` content our class object with all the methods and variable. 
- `main.py` is the file to run if you want to play the game. It content the gaming loop. 
- `words_list.txt` is the file where the words are stocked. If you want to add more words in the pool, this is the place where to add. 

## Usage

To play the game, you just have to type that command in the terminal. 

```bash
python main.py
```
If it's note working, you can try:

```bash
py main.py
```
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)