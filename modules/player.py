import random
from .tiles import Tile as tile
from .log import moveLog as moveLog

random.seed(a=None, version=2)

class Player:
    def __init__(self, playerID, balance=1500, ownedProperty=[], icon="", position=0, inJail=False, getOutOfJailCardCount=0):
        self.playerID = playerID
        self.icon = icon
        self.balance = balance
        self.ownedProperty = ownedProperty
        self.position = 0 
        self.position = position
        self.inJail = inJail
        self.getOutOfJailCardCount = 0

    def sendTrade(self, receiver):
        # select ownedProperty, balance, getOutOfJailCardCount self sends to P2, add balance to array first
        offerSender = []
        # select ownedProperty, balance, getOutOfJailCardCount self receives from P2, add balance to array first
        offerReceiver = []
        # send playerID of self
        sendPressed = False
        if(sendPressed):
            receiver.receiveTrade(self, offerSender, offerReceiver, self.playerID)
            offerSender = []
            offerReceiver = []
    
    def receiveTrade(self, offerSender, offerReceiver, senderID):
        # display offer
        # wait for acceptance/refusal
        accepted = False
        refused = False
        if(accepted):
            self.balance += offerSender[0]
            senderID.balance -= offerSender[0]
            self.balance -= offerReceiver[0]
            senderID.balance += offerReceiver[0]
            moveLog.append("p" + str(self.playerID) + " accepted an offer from p" + str(senderID))
            # output an "Offer Accepted" message
        if(refused):
            moveLog.append("p" + str(self.playerID) + " refused an offer from p" + str(senderID))
            # ouput an "Offer Refused" message

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


def initialize(icons):
    playerArr = []

    for i in range(len(icons)): # length of icons represents the number of players
        newPlayer = Player(i, icon=icons[i])
        playerArr.append(newPlayer)
    
    return playerArr