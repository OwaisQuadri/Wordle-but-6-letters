# spinoff of wordle
# the word used for automated testing is "WORDLE"
# ask user for 6 letter word
import random
import colour

HOW_TO_PLAY = colour.DEFAULT+"Guess a 6 letter word, \nthe correct letters will appear "+colour.GREEN+"GREEN"+colour.DEFAULT + \
    ",\nthe correct letters in the incorrect spot will appear "+colour.YELLOW + \
    "YELLOW"+colour.DEFAULT+",\nand incorrect letters will appear " + \
    colour.RED+"RED"+colour.DEFAULT
MAX_GUESSES = 6
WORD_LEN = 6


class Wordify:

    word_list = list(open('wordlist.txt'))
    word = random.choice(word_list).lower()

    def __init__(self):
        pass

    def render(self, wordify):
        # portray words wrt correct word
        color_order=""
        output = ""
        for i in range(WORD_LEN):
            if wordify[i] == self.word[i]:
                # correct
                output += colour.GREEN+wordify[i].upper()+colour.DEFAULT
                color_order+="green"
            elif wordify[i] in self.word:
                # incorrect spot
                output += colour.YELLOW+wordify[i].upper()+colour.DEFAULT
                color_order+="yellow"
            else:
                # incorrect letter
                output += colour.RED+wordify[i].upper()+colour.DEFAULT
                color_order+="red"
        return (output,color_order)

    def guess(self, num, guessed_word=None):
        if num == MAX_GUESSES:
            return "The word was: "+self.word
        else:
            if guessed_word is None:
                print("Please guess a 6 letter word: " +
                      str(num+1)+"/"+str(MAX_GUESSES))
                guessed_word = input()
                
            guessed_word = guessed_word.lower()

            len_guessed = len(guessed_word)
            if len_guessed != WORD_LEN:
                return self.guess(num)
            else:
                print(self.render(guessed_word)[0])
                if guessed_word in self.word:
                    # win
                    return ('Congrats! you successfully got the word in ' + str(num+1) + '/' + str(MAX_GUESSES) + ' tries!')
                else:
                    return self.guess(num+1)

    def rigged_to(self, word):
        if len(word) == 6:
            self.word = word.lower()
        return "the word was changed to " + self.word

    def start(self):
        # prompt user for inputs and how to play
        print(colour.DEFAULT+"------- WORDIFY -------")
        print(HOW_TO_PLAY)
        print(self.guess(0))


if __name__ == '__main__':
    game = Wordify()
    game.start()
