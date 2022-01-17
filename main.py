import modules.cards as cardManager
import modules.tiles as tilesManager
import modules.player as playerManager
import modules.UIManager as UIM


""" Variable initializations """

cards = {
  "chest": cardManager.initialize("chest"),
  "chance": cardManager.initialize("chance")
}

tiles = tilesManager.initalizeProperty()
# print(tiles["1"].property.description)

icons = [] # must be defined in the selection screen, when choosing icons
players = playerManager.initialize(icons)

# print(cards["chest"][2].description)

""" Game Logic """
def EndTurn():
    pass

""" UI Code"""

import tkinter as tk
from functools import partial # for passing functions and their args

mainWindow = tk.Tk()
mainWindow.title('Monopoly')
mainWindow.geometry("720x405")

UIM.OpenMenuWindow(mainWindow) # all the code that is needed. The rest is run through UIManager.py

# mainWindow.after(1, UIM.OpenStatWindow, mainWindow)

mainWindow.mainloop() # run window forever



