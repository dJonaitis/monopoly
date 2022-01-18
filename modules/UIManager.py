import tkinter as tk
from functools import partial # for passing functions and their args
from . import game

HEADER1 = ("Arial", 24)
HEADER2 = ("Arial", 18)
PARAGRAPH = ("Arial", 12)

RED = ( 255, 0, 0)
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)

def ClearWindow(window):
  for widget in window.winfo_children(): # for each element in page
    widget.destroy() # destroy it
  return window


def Exit(window):
  window.destroy() # closes the window

def OpenStatWindow(window):
  statWindow = tk.Toplevel(window) # idk what this does
  statWindow.title('Stats')
  statWindow.geometry('200x405')

  tk.Label(statWindow, text="Your stats", font=HEADER2).pack()
  tk.Label(statWindow, text="Balance: 0", font=PARAGRAPH).pack()
  tk.Label(statWindow, text="Your property", font=HEADER2).pack()
  tk.Label(statWindow, text="(None)", font=PARAGRAPH).pack()

def OpenPlayerSelect(window):
  counter = 2 # used for tracking how many players needed
  
  def ChangeCounter(changer, label):
    nonlocal counter # needed to reference variable above, cuz python is dumb
    counter += changer

    if (counter > 8): # can't have more than 8 
      counter = 8
    elif (counter < 2): # can't have less than 2
      counter = 2

    label.config(text=str(counter)) # changes the text of the label to update counter

  ClearWindow(window)

  tk.Label(window, text="Player Select", font=HEADER1).pack()
  tk.Label(window, text="How many players are playing? (Max: 8)", font=HEADER2).pack()

  label = tk.Label(window, text="2", font=PARAGRAPH) # creates label object
  tk.Button(window, text='+', command=partial(ChangeCounter,1, label)).pack()
  label.pack() # renders label object after first button object
  tk.Button(window, text='-', command=partial(ChangeCounter,-1, label)).pack()

  tk.Button(window, text='Continue', command=partial(OpenGameWindow, window)).pack()
  tk.Button(window, text='Back', command=partial(OpenMenuWindow, window)).pack()


def LoadPropertyUI(window):
  pass

# the main board window; where the magic happens:
def OpenGameWindow(window):
  ClearWindow(window)

  tk.Label(window, text="Monopoly", font=HEADER1).pack()

  for i in range(len(game.tiles)):
    t = game.tiles[i] # tile instance

    if (t.type == "property"):
      game.tiles[i].label = tk.Label(text=t.name, fg=t.property.color, font=PARAGRAPH)
      # game.tiles[i].label = tk.Label(text=t.name, font=PARAGRAPH)
    else:
      game.tiles[i].label = tk.Label(text=t.name, font=PARAGRAPH)

    game.tiles[i].label.pack()

  LoadPropertyUI(window)
  # TODO: Start the game somehow???

  OpenStatWindow(window) # separate window for stats: balance, properties owned, etc.


def OpenCreditsWindow(window):
  window = ClearWindow(window)
  tk.Label(window, text="Credits", font=HEADER1).pack()
  tk.Label(window, text="Vincentas Danys", font=HEADER2).pack()
  tk.Label(window, text="Game Logic, UI Engine", font=PARAGRAPH).pack()

  tk.Label(window, text="Danielius Jonaitis", font=HEADER2).pack()
  tk.Label(window, text="Game Logic, Game Design", font=PARAGRAPH).pack()

  tk.Label(window, text="Vejas Balciunas", font=HEADER2).pack()
  tk.Label(window, text="UI Engine", font=PARAGRAPH).pack()

  tk.Label(window, text="Simonas Goda", font=HEADER2).pack()
  tk.Label(window, text="Game Logic, Game Design", font=PARAGRAPH).pack()

  tk.Button(window, text="Back", command=partial(OpenMenuWindow, window)).pack()
  return window

def OpenMenuWindow(window):
  ClearWindow(window)

  tk.Label(window, text="Monopoly: Cookie Factory Edition", font=HEADER1).pack()
  tk.Button(window, text='Play', command=partial(OpenPlayerSelect, window)).pack()
  tk.Button(window, text='Credits', command=partial(OpenCreditsWindow,window)).pack()
  tk.Button(window, text='Quit', command=partial(Exit, window)).pack()