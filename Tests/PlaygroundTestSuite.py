
import sys; import pprint
pprint.pprint(sys.path)

from Game.Playground import Playground
import unittest

class SelfDrivingCarTest(unittest.TestCase):

    def setUp(self):

        self.playground = Playground(7)
        print(self.playground.board.toString())


if __name__ == '__main__':
    playground = Playground(7)
    playground.outputFinalState("test1")
    unittest.main()