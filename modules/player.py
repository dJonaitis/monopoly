import random
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

        for i in range (3):
            roll1 = random.randint(min, max)
            roll2 = random.randint(min, max)

            if(not self.inJail):
                self.position += roll1 + roll2

            if(roll1 == roll2 and self.inJail):
                self.inJail = False
                self.position += roll1 + roll2
                return

            if(roll1 != roll2):
                return
            


def loadPlayers(self, playerNum):
    players = []

    for i in range(playerNum):
        user = Player(i)
        players.append(user)
    
    return players