# spinoff of wordle
# ask user for 6 letter word
import random
COLOR_ = "\033[1;37;40m"
COLOR_GREEN = "\033[1;32;40m"
COLOR_RED = "\033[1;31;40m"
COLOR_YELLOW = "\033[1;33;40m"

HOW_TO_PLAY = COLOR_+"Guess a 6 letter word, \nthe correct letters will appear "+COLOR_GREEN+"GREEN"+COLOR_ + \
    ",\nthe correct letters in the incorrect spot will appear "+COLOR_YELLOW + \
    "YELLOW"+COLOR_+",\nand incorrect letters will appear "+COLOR_RED+"RED"+COLOR_
MAX_GUESSES = 6
WORD_LEN = 6

word_list = list(open('wordlist.txt'))
word = random.choice(word_list).lower()


def leave():
    # reveal word
    print("The word was: "+word)
    # exit


def render(wordify):
    # portray words wrt correct word

    output = ""
    for i in range(WORD_LEN):
        if wordify[i] == word[i]:
            # correct
            output += COLOR_GREEN+wordify[i].upper()+COLOR_
        elif wordify[i] in word:
            # incorrect spot
            output += COLOR_YELLOW+wordify[i].upper()+COLOR_
        else:
            # incorrect letter
            output += COLOR_RED+wordify[i].upper()+COLOR_
    print(output)


def guess(num):
    if num == MAX_GUESSES-1:
        leave()
    else:
        print("Please guess a 6 letter word: ")
        guessed_word = input()
        guessed_word = guessed_word.lower()
        len_guessed = len(guessed_word)
        if len_guessed != WORD_LEN:
            guess(num)
        else:
            render(guessed_word)
            if guessed_word in word:
                # win
                print(
                    'Congrats! you successfully got the word in', num+1, '/', MAX_GUESSES, ' tries!')
            else:
                guess(num+1)


def start():
    # prompt user for inputs and how to play
    print(COLOR_+"------- WORDIFY -------")
    print(HOW_TO_PLAY)
    guess(0)


if __name__ == '__main__':
    start()
