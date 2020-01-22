from Game.Player import Player
from Game.Item import Item
from Game.Board import Board
from Game.Constants import *
from collections import deque, OrderedDict
import json


class Playground:
    # def __init__(self, boardDimension, players, items):
    #     self.boardDimension = boardDimension
    #     self.players = players
    #     self.items = items
    #     self.board = Board(self.boardDimension, self.players, self.items)

    def __init__(self, boardDimension):
        self.boardDimension = boardDimension
        self.players = self.generateDefaultPlayers()
        self.items = self.generateDefaultItems()
        self.board = Board(self.boardDimension, self.players, self.items)
        self.currentPlayer = self.players[0]
        self.moves = self.importMoveListFromFile("test1")
        self.finalState = self.generateFinalState()

    def readMove(self, move):
        splitMove = move.split(":")
        if (len(splitMove) == 2):
            playerString = splitMove[0]
            directionString = splitMove[1]
        else:
            # Handle invalid move string
            print("Invalid move String...", move)
            return

        if (playerString == "R"):
            playerToMove = self.players[0]
        elif (playerString == "B"):
            playerToMove = self.players[1]
        elif (playerString == "G"):
            playerToMove = self.players[2]
        elif (playerString == "Y"):
            playerToMove = self.players[3]
        else:
           # Handle invalid player string
            print("Invalid player String...", move)
            return

        if (directionString == "N"):
            direction = Directions.NORTH
        elif (directionString == "E"):
            direction = Directions.EAST
        elif (directionString == "S"):
            direction = Directions.SOUTH
        elif (directionString == "W"):
            direction = Directions.WEST
        else:
           # Handle invalid direction string
            print("Invalid direction String...", move)
            return

        self.processMove(playerToMove, direction)
        print(self.board.toStringDeaths(self.players))


    def processMove(self, playerToMove, direction):
        # Process single move in current board state
        # move: (Player, Direction)
        # Check if player is still alive
        if (playerToMove.status == Status.DROWNED):
            print("Player", playerToMove.name, "has already drowned and cannot move!")
            return
        elif (playerToMove.status == Status.DEAD):
            print("Player", playerToMove.name, "has already been killed and cannot move!")
            return

        self.board.removeFromBoard(playerToMove)

        originalXPos = playerToMove.xPos
        originalYPos = playerToMove.yPos
        playerToMove.makeMove(direction)

        # Check if player has drowned
        if self.checkPlayerOutOfBounds(playerToMove):
            originalBoardPosition = self.board.board[originalYPos][originalXPos]
            playerToMove.dropCurrentItem(originalBoardPosition)

            playerToMove.attack = 0
            playerToMove.defence = 0
            playerToMove.status = Status.DROWNED

            print("Player", playerToMove.name, "has drowned!")

            return

        self.board.placePlayerInNewPosition(playerToMove)


        # Check if player has picked up item


        # Check if player has engaged in battle

    def proccessNewPlayerPosition(self, currentPlayer):
        if (self.checkPlayerOutOfBounds(currentPlayer)):
            currentPlayer.status = Status.DROWNED
            return
        else:
            self.board.addToBoard(currentPlayer)

    def checkPlayerOutOfBounds(self, currentPlayer):
        return currentPlayer.xPos < 0 or currentPlayer.xPos >= self.boardDimension or currentPlayer.yPos < 0 or currentPlayer.yPos >= self.boardDimension

    def generateDefaultPlayers(self):
        defaultPlayers = []

        redPlayer = Player("red", "R", Status.LIVE, 0, 0, None, 0, 0)
        bluePlayer = Player("blue", "B", Status.LIVE, 0, 7, None, 0, 0)
        greenPlayer = Player("green", "G", Status.LIVE, 7, 7, None, 0, 0)
        yellowPlayer = Player("yellow", "Y", Status.LIVE, 7, 0, None, 0, 0)

        defaultPlayers.extend([redPlayer, bluePlayer, greenPlayer, yellowPlayer])

        return defaultPlayers

    def generateDefaultItems(self):
        defaultItems = []

        axeItem = Item(ItemType.AXE, "A", 2, 2, 2, 0)
        daggerItem = Item(ItemType.DAGGER, "D", 2, 5, 1, 0)
        HelmetItem = Item(ItemType.HELMET, "H", 5, 5, 0, 1)
        magicStaffItem = Item(ItemType.MAGICSTAFF, "M", 5, 2, 1, 1)

        defaultItems.extend([axeItem, daggerItem, HelmetItem, magicStaffItem])

        return defaultItems

    def importMoveListFromFile(self, fileName):
        with open("Tests/TestFiles/Input/" + fileName + ".txt") as f:
            content = f.readlines()
        return [x.strip() for x in content]

    def processMoves(self):
        self.board = Board(self.boardDimension, self.players, self.items)

        movesQueue = deque(self.moves)
        if (movesQueue.popleft() != "GAME-START"):
            # TODO Handle invalid entry error
            print("Invalid moves file")

        while len(movesQueue) > 0:
            move = movesQueue.popleft()
        # for move in iter(movesQueue.popleft, None):
            if (move == "GAME-END"):
                print("GAME-END... Game has finished")
                print(self.board.toStringDeaths(self.players))
            else:
                self.readMove(move)

    def generateFinalState(self):
        self.processMoves()

        finalState = OrderedDict()
        for player in self.players:
            playerArr = []
            if (player.status == Status.DROWNED):
                playerArr.append(None)
            else:
                playerArr.append([player.yPos, player.xPos])
            playerArr.append(player.status.name)
            playerArr.append(player.item)
            playerArr.append(player.calculateAttack())
            playerArr.append(player.calculateDefence())

            finalState[player.name] = playerArr

        for item in self.items:
            itemArr = []
            itemArr.append([item.yPos, item.xPos])
            itemArr.append(item.playerEquipped)

            finalState[item.name.name] = itemArr

        return finalState

    def outputFinalState(self, fileName):
        with open("Tests/TestFiles/Output/" + fileName + "_final_state.json", 'w') as f:
            json.dump(self.finalState, f, ensure_ascii=False, indent=4)

    def movementTest(self):
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.SOUTH)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.SOUTH)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        print(self.board.toStringDeaths(self.players))
        # self.processMove(self.players[0], Directions.NORTH)
        # print(self.board.toStringDeaths(self.players))
        # self.processMove(self.players[0], Directions.NORTH)
        # print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))
        self.processMove(self.players[0], Directions.EAST)
        print(self.board.toStringDeaths(self.players))



# if __name__ == "__main__":
#     playground = Playground(8)
#     # playground.movementTest()
#     # playground.importMoveListFromFile("test1.txt")
#     # playground.processMoves()
#     playground.outputFinalState("test1")
#     # print(playground.moves)
