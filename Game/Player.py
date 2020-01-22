from Constants import Directions, Status, ItemType

class Player:
    def __init__(self, colour, boardPiece, status, xPos, yPos, item, attack, defence):
        self.colour = colour
        self.boardPiece = boardPiece
        self.status = status
        self.xPos = xPos
        self.yPos = yPos
        self.item = item
        self.attack = attack
        self.defence = defence

        self.name = colour
        self.age = 22

    def makeMove(self, direction):
        if (direction == Directions.NORTH):
            self.yPos -= 1
        elif (direction == Directions.EAST):
            self.xPos += 1
        elif (direction == Directions.SOUTH):
            self.yPos += 1
        elif (direction == Directions.WEST):
            self.xPos -= 1

        if (self.item != None):
            self.item.makeMove(direction)

    def findBestItemOnBoardPosition(self, boardPosition):
        if self.item == None:
            # TODO Change to not pickup and drop items every time
            availableItems = boardPosition.items.copy()
            for availableItem in availableItems:
                if (self.item == None or availableItem.name > self.item.name):
                    self.dropCurrentItem(boardPosition)
                    self.pickupItem(boardPosition, availableItem)

    def dropCurrentItem(self, boardPosition):
        if (self.item != None):
            boardPosition.addObjectToBoardPosition(self.item)
            self.item = None

    def pickupItem(self, boardPosition, itemToPickup):
        if (self.item == None):
            self.item = boardPosition.removeObjectFromBoardPosition(itemToPickup)
        else:
            # TODO Handle item already equipped error
            print("Player already has an equipped item")

    def attackBoardPosition(self, boardPosition):
        currentBoardPositionPlayers = boardPosition.players.copy()
        for defendingPlayer in currentBoardPositionPlayers:
            if self != defendingPlayer:
                print("Attacking player!")
                boardPosition.runFight(self, defendingPlayer)

    def calculateAttack(self):
        if (self.item != None):
            return self.attack + self.item.attackModifier
        else:
            return self.attack

    def calculateDefence(self):
        if (self.item != None):
            return self.defence + self.item.defenceModifier
        else:
            return self.defence

    def isAlive(self):
        return self.status == Status.LIVE

    def isDead(self):
        return self.status == Status.DEAD

    def isDrowned(self):
        return self.status == Status.DROWNED

    def toString(self):
        if self.status == Status.LIVE:
            return self.boardPiece
        else:
            return self.boardPiece.lower()
