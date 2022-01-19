import modules.UIManager as UIM

""" UI Code """

import tkinter as tk
from functools import partial # for passing functions and their args

mainWindow = tk.Tk()
mainWindow.title('Monopoly')
mainWindow.geometry("720x920")

UIM.OpenMenuWindow(mainWindow) # all the code that is needed. The rest is run through UIManager.py

# mainWindow.after(1, UIM.OpenStatWindow, mainWindow)

mainWindow.mainloop() # run window forever



