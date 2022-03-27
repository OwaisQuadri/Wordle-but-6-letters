#dynamic slice for the variable 'color_order' : when the word is 'wordle' and it is solved in 1 guess
class Wordify:
    word = "wordle"
    def __init__(self):
        pass
    def render(self, wordify):
        # portray words wrt correct word
        color_order=""
        for i in range(6):
            if wordify[i] == self.word[i]:
                # correct
                color_order+="green"
        return (color_order)
    def guess(self, guessed_word=None):
        print(self.render(guessed_word))
        if guessed_word in self.word:
            # win
            return (guessed_word)
    def start(self):
        print(self.guess("wordle"))
if __name__ == '__main__':
    game = Wordify()
    game.start()
