class Property:
    def __init__(self,price,housePrice,color,name,rentCost,ownerID=-1):
        self.price = price
        self.ownerID = ownerID # -1 by default, meaning no owner
        self.housePrice = housePrice
        self.color = color
        self.name = name
        self.housePrice = housePrice
        self.rentCost = rentCost

propertyNumber = 28 #total number of all purchasable properties

#define data above

class Tile:
    def __init__(self,tileID,type,property):
        self.tileID = tileID
        self.type = type
        self.property = property