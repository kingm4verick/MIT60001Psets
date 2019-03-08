# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string


WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in
    letters_guessed; False otherwise
    '''
    secret_wordlist = []
    for letter in secret_word:
        secret_wordlist.append(letter)

    if sorted(secret_wordlist) == sorted(letters_guessed):
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that
    represents which letters in secret_word have been guessed so far.
    '''
    new_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            new_word += letter
        else:
            new_word += '_ '
    return new_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which
    letters have not yet been guessed.
    '''
    available_letters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            available_letters += letter
    return available_letters


def warning_text(warning):
    '''Returns string based on warnings remaining'''
    if warning == 2:
        print('You have %s warning left.' % str((3 - warning)))
    elif warning > 3:
        print('You have no warnings left, so you lose a guess: ', end='')
    else:
        print('You have %s warnings left.' % str((3 - warning)))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_exhausted = []
    letters_guessed = []
    guess = 6
    warning = 1
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) +
          ' letters long.')

    while (is_word_guessed(secret_word, letters_guessed) is False) and\
          (guess > 0):
        print('-------------')
        if len(letters_exhausted) == 0 and guess == 6:
            print('You have %s warnings left' % (str(warning + 2)))
        if guess == 1:
            print('You have ' + str(guess) + ' guess left.')
        else:
            print('You have ' + str(guess) + ' guesses left.')
        print('Available letters: ' + get_available_letters(letters_exhausted))
        char = ''

        while True:
            char = input('Please guess a letter: ').lower().strip()

            if not char.isalpha() or char in letters_guessed:
                if warning <= 3:
                    if not char.isalpha():
                        letters_exhausted.append(char)
                        print('WARNING #' + str(warning) + ' : That is not a' +
                              ' valid letter! ', end='')
                        print(get_guessed_word(secret_word, letters_guessed))
                        warning_text(warning)
                        warning += 1
                    else:
                        print('WARNING #' + str(warning) + ' : You have al' +
                              'ready picked that letter. ', end='')
                        print(get_guessed_word(secret_word, letters_guessed))
                        warning_text(warning)
                        warning += 1
                    break

                else:
                    warning_text(warning)
                    print(get_guessed_word(secret_word, letters_guessed))
                    guess -= 1
                    break

            else:
                if char in secret_word and len(char) == 1:
                    for letter in secret_word:
                        if letter == char:
                            letters_guessed.append(char)
                            letters_exhausted.append(char)
                    print('Good guess:',
                          get_guessed_word(secret_word, letters_guessed))
                    break
                elif len(char) > 1:
                    if warning <= 3:
                        letters_exhausted.append(char)
                        print('WARNING #' + str(warning) + ' : Input only ' +
                              'single letters. ', end='')
                        print(get_guessed_word(secret_word, letters_guessed))
                        warning_text(warning)
                        warning += 1
                    else:
                        warning_text(warning)
                        print(get_guessed_word(secret_word, letters_guessed))
                        guess -= 1
                    break
                else:
                    if char not in letters_exhausted:
                        print('Oops: That letter is not in my word: ', end='')
                        letters_exhausted.append(char)
                        print(get_guessed_word(secret_word, letters_guessed))
                        if char not in 'aeiou':
                            guess -= 1
                        else:
                            guess -= 2
                    else:
                        if warning <= 3:
                            print('WARNING #' + str(warning) + ' : You have ' +
                                  'already picked that letter and it is not ' +
                                  'in the word: ', end='')
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            warning_text(warning)
                            warning += 1
                        else:
                            warning_text(warning)
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            guess -= 1
                    break

    if guess <= 0 and not is_word_guessed(secret_word, letters_guessed):
        print('-------------')
        print('Sorry you ran out of guesses, the word was:', secret_word)
    else:
        total_score = guess * len(set(secret_word))
        print('-------------')
        print('Congratulations, you won!')
        print('Your Total Score for this game is: ' + str(total_score) + '.')

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
       corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    new_word = ''
    for letter in my_word:
        if letter.isalpha() or letter == '_':
            new_word += letter

    if len(new_word) != len(other_word):
        return False

    else:
        letter_count = 0
        letters_common = 0
        for letter in new_word:
            if letter.isalpha():
                letter_count += 1

        for i in range(len(new_word)):
            if new_word[i] == other_word[i]:
                if other_word.count(other_word[i]) == \
                   new_word.count(new_word[i]):
                    letters_common += 1
                else:
                    return False

        if letter_count == letters_common:
            return True
        else:
            return False


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches
    my_word
    Keep in mind that in hangman when a letter is guessed, all the positions
    at which that letter occurs in the secret word are revealed.
    Therefore, the hidden letter(_ ) cannot be one of the letters in the word
    that has already been revealed.

    '''
    match_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_list.append(word)

    if len(match_list) == 0:
        print('No matches found.', end='')
    else:
        print('Possible word matches are:')
        # for word in match_list:
        #     print(word, end='  ')
        for i in range(0, len(match_list), 5):
            print(('   '.join(match_list[i:i + 6]).strip(', ')))


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    Starts up an interactive game of Hangman.
    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.
    * The user should start with 6 guesses
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    * Ask the user to supply one guess per round. Make sure to check that the
     user guesses a letter
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each guess, you should display to the user the
      partially guessed word so far.
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.
    Follows the other limitations detailed in the problem write-up.
    '''
    letters_exhausted = []
    letters_guessed = []
    guess = 6
    warning = 1
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) +
          ' letters long.')

    while (is_word_guessed(secret_word, letters_guessed) is False) and\
          (guess > 0):
        print('-------------')
        if len(letters_exhausted) == 0 and guess == 6:
            print('You have %s warnings left' % (str(warning + 2)))
        if guess == 1:
            print('You have ' + str(guess) + ' guess left.')
        else:
            print('You have ' + str(guess) + ' guesses left.')
        print('Available letters: ' + get_available_letters(letters_exhausted))
        char = ''

        while True:
            char = input('Please guess a letter: ').lower().strip()

            if char != '*':
                if not char.isalpha() or char in letters_guessed:
                    if warning <= 3:
                        if not char.isalpha():
                            letters_exhausted.append(char)
                            print('WARNING #' + str(warning) + ' : That ' +
                                  'is not a valid letter! ', end='')
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            warning_text(warning)
                            warning += 1
                        else:
                            print('WARNING #' + str(warning) + ' : You have ' +
                                  'already picked that letter. ', end='')
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            warning_text(warning)
                            warning += 1
                        break

                    else:
                        warning_text(warning)
                        print(get_guessed_word(secret_word, letters_guessed))
                        guess -= 1
                        break

                else:
                    if char in secret_word and len(char) == 1:
                        for letter in secret_word:
                            if letter == char:
                                letters_guessed.append(char)
                                letters_exhausted.append(char)
                        print('Good guess:',
                              get_guessed_word(secret_word, letters_guessed))
                        break
                    elif len(char) > 1:
                        if warning <= 3:
                            letters_exhausted.append(char)
                            print('WARNING #' + str(warning) + ' : Input ' +
                                  'only single letters. ', end='')
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            warning_text(warning)
                            warning += 1
                        else:
                            warning_text(warning)
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            guess -= 1
                        break
                    else:
                        if char not in letters_exhausted:
                            print('Oops: That letter is not in my word: ',
                                  end='')
                            letters_exhausted.append(char)
                            print(get_guessed_word(secret_word,
                                  letters_guessed))
                            if char not in 'aeiou':
                                guess -= 1
                            else:
                                guess -= 2
                        else:
                            if warning <= 3:
                                print('WARNING #' + str(warning) + ' : You' +
                                      ' have already picked that letter and' +
                                      ' it is not in the word: ', end='')
                                print(get_guessed_word(secret_word,
                                      letters_guessed))
                                warning_text(warning)
                                warning += 1
                            else:
                                warning_text(warning)
                                print(get_guessed_word(secret_word,
                                      letters_guessed))
                                guess -= 1
                        break
            else:
                show_possible_matches(get_guessed_word(secret_word,
                                      letters_guessed))
                print('-------------')

    if guess <= 0 and not is_word_guessed(secret_word, letters_guessed):
        print('-------------')
        print('Sorry you ran out of guesses, the word was:', secret_word)
    else:
        total_score = guess * len(set(secret_word))
        print('-------------')
        print('Congratulations, you won!')
        print('Your Total Score for this game is: ' + str(total_score) + '.')


# When you've completed your hangman_with_hint function, comment the two
# similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
    while True:
        game_type = int(input('Choose game mode:\n1. Classic Hangman\n2. H' +
                        'angman with hints\n3.Exit\n-------------'))
        if game_type == 1:
            secret_word = choose_word(wordlist)
            hangman(secret_word)
            req = input('Do you wish to play again (y/n)? ').strip().lower()
            if req == 'y':
                continue
            elif req == 'n':
                break
            else:
                print('Invalid submission')
                break
        elif game_type == 2:
            secret_word = choose_word(wordlist)
            hangman_with_hints(secret_word)
            req = input('Do you wish to play again (y/n)? ').strip().lower()
            if req == 'y':
                continue
            elif req == 'n':
                break
            else:
                print('Invalid submission')
                break
        elif game_type == 3:
            break
        else:
            print('Invalid Submission.')
            break
