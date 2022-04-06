import random


HANGMAN = [
    '________',
    '|       |',
    '|       O',
    '|       |',
    '|      /|\ ',
    '|       |',
    '|      / \ '
]

WORDS = [
    'PYTHON', 'JAVA', 'HTML', 'CSS', 'COMPUTER', 'LOTR',
    'RONALDO', 'LAPTOP', 'BROWSER', 'LOGITECH', 'APPLE'
]

class Hangman():
    """
    Hangman game
    """

    def __init__(self,word_to_try):
        self.failed_attempts = 0
        self.word_to_try = word_to_try
        self.game_progress = list('_' * len(self.word_to_try))

    def locate_index(self,letter):
        """
        Takes a letter and returns a list with indexes in the word to guess
        """
        return [i for i, char in enumerate(self.word_to_try) if letter == char]
    
    