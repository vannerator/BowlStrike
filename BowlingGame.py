
class BowlingGame:
    """Class for Bowling Game logic."""

    def __init__(self):
        """Initialise list of rolls."""
        self.rolls=[]

    def roll(self,pins):
        """Add roll score to rolls list."""
        self.rolls.append(pins)

    def score(self):
        """Calculate and return game score."""
        result = 0
        rollIndex = 0

        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
        return result

    def isStrike(self, rollIndex):
        """Check to see if strike has been scored."""
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        """Check to see if spare has been scored."""
        return self.rolls[rollIndex] + self.rolls[rollIndex+1] == 10

    def strikeScore(self,rollIndex):
        """Return score for a strike and the following 2 rolls."""
        return  10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self,rollIndex):
        """Return score for a spare and the following roll."""
        return  10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        """Return score for a normal frame."""
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
