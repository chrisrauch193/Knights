from Item import Item
from Player import Player
from Constants import ItemType, ATTACK_BONUS, Status
from collections import OrderedDict

class BoardPosition:
    def __init__(self):
        self.items = set()
        self.players = set()
        self.deadPlayers = set()

    def addObjectToBoardPosition(self, gameObject):
        if isinstance(gameObject, Item):
            self.items.add(gameObject)
            gameObject.playerEquipped = False

            for player in self.players:
                player.findBestItemOnBoardPosition(self)
        elif isinstance(gameObject, Player):
            if gameObject.isAlive():
                self.players.add(gameObject)
                gameObject.findBestItemOnBoardPosition(self)
                gameObject.attackBoardPosition(self)
            elif gameObject.isDead():
                self.deadPlayers.add(gameObject)
            else:
                # TODO: Handle errors
                print("Error invalid boardPiece")
        else:
            # TODO: Handle errors
            print("Error invalid boardPiece")

    def removeObjectFromBoardPosition(self, gameObject):
        if isinstance(gameObject, Item):
            gameObject.playerEquipped = True
            self.items.remove(gameObject)
            return gameObject
        if isinstance(gameObject, Player):
            if gameObject.isAlive():
                self.players.remove(gameObject)
                return gameObject
            elif gameObject.isDead():
                self.deadPlayers.remove(gameObject)
                return gameObject
            else:
                # TODO: Handle errors
                print("Error invalid boardPiece")
        else:
            # TODO handle invalid item error
            print("Invalid Item error")
            return None

    def runFight(self, attacker, defender):
        # Do battle
        attackerScore = ATTACK_BONUS + attacker.calculateAttack()
        defenderScore = defender.calculateDefence()

        if (attackerScore > defenderScore):
            self.killPlayer(defender)
            attacker.findBestItemOnBoardPosition(self)
        else:
            self.killPlayer(attacker)
            defender.findBestItemOnBoardPosition(self)

    def killPlayer(self, playerToKill):
        print("Killing", playerToKill.name, "Player")
        playerToKill.dropCurrentItem(self)
        playerToKill.attack = 0
        playerToKill.defence = 0
        self.players.remove(playerToKill)
        playerToKill.status = Status.DEAD
        self.deadPlayers.add(playerToKill)

    def getOrderedItems(self):
        orderedItems = OrderedDict()
        itemDict = dict(self.items)
        for itemType in ItemType:
            if itemType in self.items:
                orderedItems[itemType] = itemDict.pop(itemType)
        orderedItems.update(itemDict.items())
        return orderedItems

    def noPlayers(self):
        return len(self.players) == 0

    def noItems(self):
        return len(self.items) == 0

    def noDeadPlayers(self):
        return len(self.deadPlayers) == 0

    def isEmpty(self):
        return self.noPlayers() and self.noItems()

    def toString(self):
        if len(self.players) > 0:
            return next(iter(self.players)).toString()
        elif len(self.deadPlayers) > 0:
            return next(iter(self.deadPlayers)).toString()
        elif len(self.items) > 0:
            return next(iter(self.items)).toString()
        else:
            return "_"