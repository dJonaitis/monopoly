class Player:
    def __init__(self, playerID, balance, ownedProperty, icon=""):
        self.playerID = playerID
        self.icon = icon
        self.balance = balance
        self.ownedProperty = ownedProperty
        self.position = 0

players = []
