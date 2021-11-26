
import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):
    """Class for unit testing BowlingGame.py."""

    def setUp(self):
        """Initiate game."""
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        """Test for all gutter balls."""
        self.rollMany(0, 20)
        assert self.game.score()==0

    def testAllOnes(self):
        """Test for all ones."""
        self.rollMany(1, 20)
        assert self.game.score()==20

    def testOneSpare(self):
        """Test for one spare."""
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16

    def testOneStrike(self):
        """Test for one strike."""
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert self.game.score()==24

    def testPerfectGame(self):
        """Test for a perfect game (all strikes)."""
        self.rollMany(10,12)
        assert self.game.score()==300

    def testAllSpares(self):
        """Test for all spares."""
        self.rollMany(5,21)
        assert self.game.score()==150

    def rollMany(self, pins, rolls):
        """Method for inputting several rolls of the same score."""
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()