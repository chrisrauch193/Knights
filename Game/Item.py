from Constants import Directions

class Item:
    def __init__(self, name, boardPiece, xPos, yPos, attackModifier, defenceModifier):
        self.name = name
        self.boardPiece = boardPiece
        self.xPos = xPos
        self.yPos = yPos
        self.attackModifier = attackModifier
        self.defenceModifier = defenceModifier
        self.playerEquipped = None

    def makeMove(self, direction):
        if (direction == Directions.NORTH):
            self.yPos -= 1
        elif (direction == Directions.EAST):
            self.xPos += 1
        elif (direction == Directions.SOUTH):
            self.yPos += 1
        elif (direction == Directions.WEST):
            self.xPos -= 1

    def toString(self):
        return self.boardPiece