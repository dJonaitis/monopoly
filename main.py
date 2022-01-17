import modules.cards as cardManager
import modules.tiles as tilesManager
import modules.player as player


""" Variable initializations """

cards = {
  "chest": cardManager.initialize("chest"),
  "chance": cardManager.initialize("chance")
}

tiles = tilesManager.initalizeProperty()
# print(tiles["1"].property.description)

icons = [] # must be defined in the selection screen, when choosing icons
players = player.initialize(icons)

# print(cards["chest"][2].description)

""" UI Initialization"""

import uiengine as ui