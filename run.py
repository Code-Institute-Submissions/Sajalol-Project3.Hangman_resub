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
    The Hangman game
    """

    def __init__(self, word_to_try):
        self.failed_attempts = 0
        self.word_to_try = word_to_try
        self.game_progress = list('_' * len(self.word_to_try))

    def locate_indexes(self, letter):
        """
        Method that takes a letter and returns a list with his indexes in
        the word to try
        """
        return [i for i, char in enumerate(self.word_to_try) if letter == char]

    def is_invalid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter
        """
        return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

    def print_game(self):
        """
        Method to print the word to try blankspaces
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progress))

    def update_prog(self, letter, indexes):
        """
        Method to update the game progress with the guessed letters
        """
        for index in indexes:
            self.game_progress[index] = letter

    def get_user_input(self):
        user_input = input('\nType a letter: ')
        return user_input

    def play(self):
        """
        Def to play the game, asking user for letter and plays the game.
        """
        while self.failed_attempts < len(HANGMAN):
            self.print_game()
            user_input = self.get_user_input()


            if self.is_invalid_letter(user_input):
                print('Input not available')
                continue

            if user_input in self.game_progress:
                print('You have already guessed that')
                continue

            if user_input in self.word_to_try:
                indexes = self.locate_indexes(user_input)
                self.update_prog(user_input, indexes)

                if self.game_progress.count('_') == 0:
                    print('You won!')
                    print('The word is: {0}'.format(self.word_to_try))
                    quit()
            else:
                self.failed_attempts += 1
        print("\n You lost")

if __name__ == '__main__':
    word_to_try = random.choice(WORDS)
    hangman = Hangman(word_to_try)
    hangman.play()