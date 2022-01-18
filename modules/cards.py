class card:
    def __init__(self, description="This card is empty. Error?", monetaryGain=0, goLocation=None, jailFree=False):
        self.description = description
        self.monetaryGain = monetaryGain
        self.goLocation = goLocation
        self.jailFree = jailFree

def initialize(cardType):

    """ This function should be run twice: once for treasure, once for chance """

    file = open(f"./assets/sheets/{cardType}_cards.tsv", "r")
    content = file.read()
    file.close()

    split = content.split('\n') # create array of each line of treausre file
    split.pop(0) # removes the header line

    cardArr = []
    for line in split: # loops through each line
        lineArr = line.split('	') # a TAB character separates values
        instance = card(lineArr[0],goLocation=lineArr[2], jailFree=bool(lineArr[3])) # creates a card object, leaves 'monetary gain' undefined
        # TODO: Add monetary gain in-game when the card is drawn. Use "".format(something=value) for formatting, and eval() to evaluate expression

        cardArr.append(instance)

    return cardArr