
import sys; import pprint
pprint.pprint(sys.path)

from Game.Playground import Playground
import unittest

class SelfDrivingCarTest(unittest.TestCase):

    def setUp(self):

        self.playground = Playground(8)
        print(self.playground.board.toString())


if __name__ == '__main__':
    # Example game test run printing board after each move
    playground = Playground(8)
    playground.outputFinalState("test1")

    # Running currently empty test suite
    unittest.main()