# import application
import unittest
import sys
sys.path.append(".")
from wordify import Wordify
import colour

class TestSum(unittest.TestCase):
    # test 1: making sure that a game exists
    def test_init(self, game=None):
        # init a wordify
        game = Wordify()
        # real, desired, failmessage
        self.assertEqual((game != None), True, "The game does not exist")
    # test 2: rig the game
    #         (make everything lowercase)
    def test_rig(self):
        # start a game
        game = Wordify()
        #rig to any word
        game.rigged_to("WoRdLe")
        self.assertEqual((game.word), "wordle", "Cannot manually set word")
    # test 3: take the correct guess
    def test_guess(self):
        # start a game
        game = Wordify()
        #rig
        game.rigged_to("wordle")
        #guess a valid word
        self.assertEqual(game.guess(0,"wordle"),"Congrats! you successfully got the word in 1/6 tries!","Did not display congrats message")
    # test 4 : make sure the colours are correctly corresponding to the character status'
    def test_render(self):
        # start a game
        game = Wordify()
        #rig
        game.rigged_to("wordle")
        #render a guess
        print(game.render("wallet"))
        self.assertEqual(game.render('wallet')[1],"greenredyellowyellowyellowred","incorrect colors")
    #test 5: testing whether a loss will reveal the true word
    def test_loss(self):
        # start a game
        game = Wordify()
        #rig
        game.rigged_to("wordle")
        #incorrect last guess
        self.assertEqual(game.guess(5,"walter"),"The word was: wordle", "Did not mention the correct word on the way out")


if __name__ == '__main__':
    unittest.main()
