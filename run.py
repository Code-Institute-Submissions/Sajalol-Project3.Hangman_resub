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

    def __init__(self, word_to_try):
        self.failed_attempts = 0
        self.word_to_try = word_to_try
        self.game_progression = list('_' * len(self.word_to_try))

    def locate_indexes(self, letter):
        """
        Takes a letter and returns a list with indexes in the word to guess
        """
        return [i for i, char in enumerate(self.word_to_try) if letter == char] 

    def is_invalid_letter(self, input_):
        """
        Method to validate if an user input is not just a letter
        """
        return input_.isdigit() or (input.isalpha() and len(input) > 1)


    def print_game(self):
        """
        Print the word to guess blankspaces remaining and attempts and guessed letters
        """
        print('\n')
        print('\n'.join(HANGMAN[:self.failed_attempts]))
        print('\n')
        print(' '.join(self.game_progression))

    
    def update_prog(self, letter, indexes):
        """
        Method to update Game progress with the guessed letters
        """
        for index in indexes:
            self.game_progression[index] = letter

    def get_user_input(self):
        user_input = input('\nType a letter: ')
        return user_input
    

    def game(self):
        """
        Def to play the game, asking user for letter and plays the game.
        """
        while self.failed_attempts < len(HANGMAN):
            self.print_game()
            user_input = self.get_user_input()

            if self.is_invalid_letter(user_input):
                print('input not available')
                continue

            if user_input in self.game_progression:
                print('You have already guessed that')
                continue

            if user_input in self.word_to_try:
                indexes = self.locate_indexes(user_input)
                self.update_prog(user_input, indexes)

                if self.game_progression.count('_') == 0:
                    print('\n You won!')
                    print('The word is: {0}'.format(self.word_to_try))
                    quit()
            else:
                self.failed_attempts += 1
                print("\n You lost")


if __name__ == '__main__':
    word_to_try = random.choice(WORDS)
    hangman = Hangman(word_to_try)
    hangman.play()