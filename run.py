import random

HANGMAN_PICS = ['''

  +---+
      |
      |
      |
     ===''', '''

  +---+
  O   |
      |
      |
     ===''', '''

  +---+
  O   |
  |   |
      |
     ===''', '''

  +---+
  O   |
 /|   |
      |
     ===''', '''

  +---+
  O   |
 /|\  |
      |
     ===''', '''

  +---+
  O   |
 /|\  |
 /    |
     ===''', '''

  +---+
  O   |
 /|\  |
 / \  |
     ===''']

WORDS = ['PYTHON', 'JAVA', 'HTML', 'CSS', 'COMPUTER', 'LOTR',
    'RONALDO', 'LAPTOP', 'BROWSER', 'LOGITECH', 'APPLE']

def get_random_word(word_list):
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]

missed_letters = ''
correct_letters = ''
secret_word = get_random_word(WORDS)
game_is_done = False

while True:
    print('Missed letters:', missed_letters)
    print('Correct letters:', correct_letters)
    print(HANGMAN_PICS[len(missed_letters)])
    
    guess = input("Guess a letter: ").upper()

    if guess in secret_word:
        correct_letters = correct_letters + guess

        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print("Yes, the secret word is " + secret_word + "! You win!")
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            print(HANGMAN_PICS[-1])
            print("You have run out of guesses!\nAfter " + str(len(missed_letters)) + " missed guesses and " + str(len(correct_letters)) + " correct guesses, the word was " + secret_word + "")
            game_is_done = True

    if game_is_done:
        if input("Do you want to play again? (yes or no)").lower().startswith('y'):
            missed_letters = ''
            correct_letters = ''
            secret_word = get_random_word(WORDS)
            game_is_done = False
        else:
            break
