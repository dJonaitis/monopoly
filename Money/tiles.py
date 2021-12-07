class Property:
    def __init__(self,propertyID,price,housePrice,color,name):
        self.propertyID = propertyID
        self.price = price
        self.housePrice = housePrice
        self.color = color
        self.name = name

propertyNumber = 28 #total number of all purchasable properties

#define data above

class Tile:
    def __init__(self,tileID,type):
        self.tileID = tileID
        self.type = type