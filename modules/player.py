import random
import tiles

tile = tiles.Tile

random.seed(a=None, version=2)

class Player:
    def __init__(self, playerID, balance=1500, ownedProperty=[], icon="", position=0, inJail=False):
        self.playerID = playerID
        self.icon = icon
        self.balance = balance
        self.ownedProperty = ownedProperty
        self.position = 0
        self.position = position
        self.inJail = inJail
    
    def roll(self):
        min = 1 
        max = 6

        for i in range (4):
            roll1 = random.randint(min, max)
            roll2 = random.randint(min, max)
            if(i == 4):
                self.inJail = True
                self.position = 10
                return
                
            if(not self.inJail):
                self.position += roll1 + roll2
                if(self.position == 30):
                    self.inJail = True
                    self.position = 10
                    return

            if(roll1 == roll2 and self.inJail):
                self.inJail = False
                self.position += roll1 + roll2
                return

            if(roll1 != roll2): 
                return


    def payRent(self,tile,landlord): #access class Tile and class Property
        if (tile.type== 'property'):
            if (tile.property.ownerID >-1 ):
                if(tile.property.ownerID != self.playerID):
                    landlord.balance += tile.property.rentCost #pay rent
                    self.balance -= tile.property.rentCost 
                    
            else: #buy property. Note to self: Add prompt to ask if you wanna buy
                self.buy(tile)

    def buyProperty(self,tile):
        self.ownedProperty = tile.tileID
        tile.property.ownerID = self.playerID
        self.balance -= tile.property.price
    
    def buyHouse(self, tile):
        tile.property.houseNumber += 1
        self.balance -= tile.property.housePrice


def initialize(playerCount, icons):
    playerArr = []

    for i in range(playerCount):
        newPlayer = Player(i, icon=icons[i])
        playerArr.append(newPlayer)
    
    return playerArr