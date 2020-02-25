# Exercise 6: Hangman
# Write a hangman game that randomly generates a word and prompts
# the user to guess one letter at a time, as shown in the sample run.
# Each letter in the word is displayed as an asterisk. When the user
# makes a correct guess, the actual letter is then displayed. When the user
# finishes a word, display the number of misses and ask the user whether to
# continue playing. Create a list to store the words, as follows:
# words = ["write", "that", "program", ...]
# (Guess) Enter a letter in word ******* > p
# (Guess) Enter a letter in word pr**r** > p
#     p is already in the word
# (Guess) Enter a letter in word pr**r** > o
# (Guess) Enter a letter in word pro*r** > g
# (Guess) Enter a letter in word progr** > n
#     n is not in the word
# (Guess) Enter a letter in word progr** > m
# (Guess) Enter a letter in word progr*m > a
# The word is program. You missed 1 time
# Do you want to guess another word? Enter y or n>

import random


def get_word():
    words = ['sinan', 'heleneeeeee', 'app']
    rnd = random.choice(words)
    star_list = ['*' for x in rnd]
    star_word = ''.join(star_list)
    return [rnd, star_word, len(rnd)]


def play_again():
    answer = input('Would you like to play again? Answer Yes/No?').lower()
    if answer == 'yes' or answer == 'y':
        main()
    else:
        pass

def main():
    actual_word, actual_stared, actual_character = get_word()
    try_life = 10  # int(actual_character * 1.5) not a good idea! long word allows user to enter whole alph!
    print(f'Lets play Hangman! The word contains {actual_character} letters: {actual_stared}')
    letters_guessed = []
    guessed = False
    message = f'(HangmanGame) Enter a letter in word {actual_stared} or a word with {actual_character} character > '
    while guessed == False and try_life > 0:
        print(f'You have {try_life} tries!')
        guess = input(f'(HangmanGame) Enter a letter in word {actual_stared} or a word with {actual_character} character > ')
        #if user enters only 1 letter
        if len(guess) == 1 and guess in letters_guessed:
            print('you have already guessed that letter!')
        elif len(guess) == 1 and guess in actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Well done it is in the word')
        elif len(guess) == 1 and guess not in actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Sorry it is NOT in the word')
        elif len(guess) != 1 and guess != actual_word:
            letters_guessed.append(guess)
            try_life -= 1
            print('Sorry it is not that word!')
        elif guess == actual_word:
            print(f'Well done! {actual_word} is the word! you WON!')
            guessed = True
        else:
            print('Sorry something went wrong, re-start the game')

        status = ''
        if guessed == False:
            for letter in actual_word:
                if letter in letters_guessed:
                    status += letter
                else:
                    status += '*'
            print(status)

        if status == actual_word:
            print('Well done you won')
            guessed = True
        elif try_life == 0:
            print('You have run out of tries before guessing the word')

    play_again()

main()
