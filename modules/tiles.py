class Property:
    def __init__(self, price=0,housePrice=0,color="none; error?",rent=[],houseNumber=0,ownerID=-1, mortgage=0):
        self.price = price
        self.ownerID = ownerID # -1 by default, meaning no owner
        self.color = color
        self.rent = rent
        self.housePrice = housePrice
        self.houseNumber = houseNumber
        self.mortgage = mortgage

propertyNumber = 28 #total number of all purchasable properties

#define data above

class Tile:
    def __init__(self,tileID=0,name="",type="",property=None, description="", label=None):
        self.tileID = tileID
        self.name = name
        self.type = type
        self.description = description
        self.property = property
        self.label = label # the UI element of the Tile

def initalizeProperty():

    file = open(f"./assets/sheets/properties.tsv", "r")
    content = file.read()
    file.close()

    split = content.split('\n') # create array of each line of treausre file
    split.pop(0) # removes the header line

    tileArr = {}
    for line in split: # loops through each line
        lineArr = line.split('	') # a TAB character separates values
        instance = Property(price=lineArr[2], mortgage=lineArr[4], rent=[lineArr[4:8]], color=lineArr[11]) # creates a property object, fills in everything
        tileInstance = Tile(tileID=lineArr[1], name=lineArr[0], type="property", description=lineArr[3], property=instance) # creates a tile instance and puts new property inside of it

        tileArr[int(lineArr[1])] = tileInstance

    return tileArr

def initializeUtility():

    file = open(f"./assets/sheets/utility.tsv", "r")
    content = file.read()
    file.close()

    split = content.split('\n')
    split.pop(0) # removes the header line

    tileArr = {}
    for line in split: # loops through each line
        lineArr = line.split('	') # a TAB character separates values
        instance = Property(price=lineArr[2], mortgage=lineArr[5]) # uses property class for transport and utility
        tileInstance = Tile(name=lineArr[0], tileID=lineArr[1], description=lineArr[3], type=lineArr[4], property=instance) # creates a tile instance and puts new property inside of it

        tileArr[int(lineArr[1])] = tileInstance

    return tileArr

def initializeMisc():

    file = open(f"./assets/sheets/tiles.tsv", "r")
    content = file.read()
    file.close()

    split = content.split('\n')
    split.pop(0) # removes the header line

    tileArr = {}
    for line in split: # loops through each line
        lineArr = line.split('	') # a TAB character separates values
        tileInstance = Tile(name=lineArr[0], tileID=lineArr[1], description=lineArr[2], type=lineArr[3]) # creates a tile instance

        tileArr[int(lineArr[1])] = tileInstance

    return tileArr