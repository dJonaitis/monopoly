#import playerNum from char select

playerNum = 2# take player num from character selection
for i in range(playerNum): #gives every player starting stats
    user = Player(i, 1500, [])
    # players.append({"playerID": user.playerID, "balance": user.balance, "ownedProperty": user.ownedProperty})
    players.append(user)
#print(players[1]["balance"])
print(players[0].balance)
