import random
import tiles

tile = tiles.Tile
prop = tiles.Property

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


    def payRent(self,tile,prop,playerNum):
        if (tile.type== 'property'):
            if (prop.ownerID >-1 ):
                if(prop.ownerID != self.playerID):
                    for i in range(playerNum): #finds owner
                        if(tile.ownerID == i): #pay rent
                            Player(i).balance += prop.rentCost
                            self.balance -= prop.rentCost
                            break
            else: #buy property. Note to self: Add prompt to ask if you wanna buy
                self.buy(tile,prop)


    def buy(self,tile,prop):
        if (tile.type == 'property'): #neccessary because this function is also for buying houses
                self.ownedProperty = tile.tileID
                self.balance -= prop.price

        #how does buying houses work?