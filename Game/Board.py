from Item import Item
from BoardPosition import BoardPosition

class Board:
    def __init__(self, size, players, items):
        self.size = size
        self.board = []
        self.resetBoard(size, players, items)

    def resetBoard(self, size, players, items):
        self.board = [[ BoardPosition() for x in range(0, self.size)] for y in range(0, self.size) ]

        for player in players:
            # TODO: Error handle placing on already filled space
            self.addToBoard(player)

        for item in items:
            # TODO: Error handle placing on already filled space
            self.addToBoard(item)
        return

    def removeFromBoard(self, gameObject):
        currentBoardPosition = self.board[gameObject.yPos][gameObject.xPos]
        currentBoardPosition.removeObjectFromBoardPosition(gameObject)

    def addToBoard(self, gameObject):
        nextBoardPosition = self.board[gameObject.yPos][gameObject.xPos]
        nextBoardPosition.addObjectToBoardPosition(gameObject)

    def placePlayerInNewPosition(self, player):
        nextBoardPosition = self.board[player.yPos][player.xPos]
        nextBoardPosition.addObjectToBoardPosition(player)

    def playerPickUpItem(self, player):
        itemOnFloor = self.board[player.yPos][player.xPos]

        if not player.item == None:
            if itemOnFloor.name > player.item.name:
                itemToDrop = player.item
                itemToDrop.player = None
                player.item = itemOnFloor
                itemOnFloor.playerEquipped = player
        else:
            player.item = itemOnFloor
            itemOnFloor.playerEquipped = player


    def toString(self):
        outString = ""
        for _ in range(self.size + 2):
            outString += "w "
        outString += "\n"
        for column in self.board:
            colString = "w"
            for object in column:
                colString += "|"
                if object == None:
                    colString += "_"
                else:
                    colString += object.toString()
            outString += colString
            outString += "|w\n"
        for _ in range(self.size + 2):
            outString += "w "
        outString += "\n"

        return outString

    def toStringDeaths(self, players):
        outString = ""
        for boardPos in range(self.size + 2):
            foundDeadPlayerInPos = False
            for player in players:
                if (player.xPos == boardPos - 1 and player.yPos < 0):
                    foundDeadPlayerInPos = True
                    outString += player.toString()
                    outString += " "
            if not foundDeadPlayerInPos:
                outString += "w "
        outString += "\n"
        for index, column in enumerate(self.board):
            colString = ""

            foundDeadPlayerInPos = False
            for player in players:
                if (player.xPos < 0 and player.yPos == index):
                    foundDeadPlayerInPos = True
                    colString += player.toString()
            if not foundDeadPlayerInPos:
                colString += "w"

            for object in column:
                colString += "|"
                if object == None:
                    colString += "_"
                else:
                    colString += object.toString()
            outString += colString

            foundDeadPlayerInPos = False
            outString += "|"
            for player in players:
                if (player.xPos >= self.size and player.yPos == index):
                    foundDeadPlayerInPos = True
                    outString += player.toString()
                    outString += "\n"
            if not foundDeadPlayerInPos:
                outString += "w\n"

        for _ in range(self.size + 2):
            foundDeadPlayerInPos = False
            for player in players:
                if (player.xPos == boardPos - 1 and player.yPos >= self.size):
                    foundDeadPlayerInPos = True
                    outString += player.toString()
                    outString += " "
            if not foundDeadPlayerInPos:
                outString += "w "
        outString += "\n"

        return outString