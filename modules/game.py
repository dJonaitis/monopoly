import modules.cards as cardManager
import modules.tiles as tilesManager
import modules.player as playerManager
import modules.UIManager as UIM
import json


""" Variable initializations """

cards = {
  "chest": cardManager.initialize("chest"),
  "chance": cardManager.initialize("chance")
}

tiles = tilesManager.initalizeProperty()
tiles = {**tiles, **tilesManager.initializeUtility()} # adds utility tiles to the dictionary
tiles = {**tiles, **tilesManager.initializeMisc()} # adds the rest of the tiles to the dictionary (corners, cards)

# file = open("debug.json", "w")
# tilesD = {}
# for element in tiles:
#   if (element.property != None):
#     element.property = element.property.__dict__()
#   tilesD[element.tileID] = element
# file.write(json.dumps(tilesD))
# file.close()


# print(tiles["1"].property.description)

icons = [] # must be defined in the selection screen, when choosing icons
players = playerManager.initialize(icons)

# print(cards["chest"][2].description)

""" Game Logic """
def EndTurn():
    pass