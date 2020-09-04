
# Hangman Game
In this game, the player must guess a random word chosen by the program. The player guesses a single letter, and if the guess is wrong, the player is one step closer to being hung by the neck.
 
* A customized words text file can be loaded or default  `short_words.txt` file can be used to select words.
* You can run the program using the instructions in *To Run* below.


### To Run

* `python3 hangman.py`
* follow the input prompts to play the game

### To Test

* To run all the unittests: `python3 -m unittest tests/test_main.py`
* To run a specific step's unittest, e.g step *1*: `python3 -m unittest tests.test_main.MyTestCase.test_step1`

