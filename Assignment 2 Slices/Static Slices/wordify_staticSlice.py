#static slice for the variable 'color_order' :
MAX_GUESSES = 6
WORD_LEN = 6
class Wordify:
    word = "wordle"
    def __init__(self):
        pass
    def render(self, wordify):
        # portray words wrt correct word
        color_order=""
        for i in range(WORD_LEN):
            if wordify[i] == self.word[i]:
                # correct
                color_order+="green"
            elif wordify[i] in self.word:
                # incorrect spot
                color_order+="yellow"
            else:
                # incorrect letter
                color_order+="red"
        return (color_order)
    def guess(self, num, guessed_word=None):
        if num != MAX_GUESSES:
            if guessed_word is None:
                print("Please guess a 6 letter word: " +
                      str(num+1)+"/"+str(MAX_GUESSES))
                guessed_word = input()
            guessed_word = guessed_word.lower()
            len_guessed = len(guessed_word)
            if len_guessed != WORD_LEN:
                return self.guess(num)
            else:
                print(self.render(guessed_word))
                if guessed_word in self.word:
                    # win
                    return (guessed_word)
                else:
                    return self.guess(num+1)
    def start(self):
        print(self.guess(0))
if __name__ == '__main__':
    game = Wordify()
    game.start()
