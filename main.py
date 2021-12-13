import graphics.colors as colors
import graphics.manager as gm
import modules.cards as cardManager
import modules.player as player

""" Variable initializations """

cards = {
  "chest": cardManager.initialize("chest"),
  "chance": cardManager.initialize("chance")
}

icons = [] # must be defined in the selection screen, when choosing icons
players = player.initialize(icons)

print(cards["chest"][3].description)
#gm.gameMenu()