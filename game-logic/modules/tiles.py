class Property:
    def __init__(self, price=0,housePrice=0,color="none; error?",name="",rent=[0,0,0,0,0,0],houseNumber=0,ownerID=-1, description="", mortgage=0):
        self.price = price
        self.ownerID = ownerID # -1 by default, meaning no owner
        self.color = color
        self.name = name
        self.description = description
        self.rent = rent
        self.housePrice = housePrice
        self.houseNumber = houseNumber
        self.mortgage = mortgage

propertyNumber = 28 #total number of all purchasable properties

#define data above

class Tile:
    def __init__(self,tileID,type,property):
        self.tileID = tileID
        self.type = type
        self.property = property

def initalizeProperty():


    file = open(f"./assets/sheets/properties.csv", "r")
    content = file.read()
    file.close()

    split = content.split('\n') # create array of each line of treausre file
    split.pop(0) # removes the header line

    tileArr = {}
    for line in split: # loops through each line
        lineArr = line.split('#') # array of elements in each card
        instance = Property(name=lineArr[0], price=lineArr[2], description=lineArr[3], mortgage=lineArr[4], rent=[lineArr[4:8]], color=lineArr[9]) # creates a property object, fills in everything
        tileInstance = Tile(lineArr[1], "property", instance) # creates a tile instance and puts new property inside of it

        tileArr[lineArr[1]] = tileInstance

    return tileArr