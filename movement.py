import random
random.seed(a=None, version=2)
def roll(player):
    min = 1 
    max = 6
    while True:
        roll1 = random.randint(min, max)
        roll2 = random.randint(min, max)
        player.position = player.position + roll1 + roll2
        if(roll1 == roll2):
            player.inJail = False
        if(roll1 != roll2):
            break