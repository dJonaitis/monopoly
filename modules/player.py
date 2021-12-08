class Player:
    def __init__(self, playerID, balance=1500, ownedProperty=[], icon="", position=0, inJail=False):
        self.playerID = playerID
        self.icon = icon
        self.balance = balance
        self.ownedProperty = ownedProperty
        self.position = 0

def loadPlayers(playerNum):
    players = []

    for i in range(playerNum):
        user = Player(i)
        players.append(user)
    
    return players