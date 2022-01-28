#log includes who, did what and where
#moveType would have to be specified in other methods for what kind of a move it should log
#moveType-s should be "bought", "paidRent", or "moved"
#"p"+ is added so its simpler for people to read when instead of just "1", "2", "3" moved to 69, it'd say p1 (player1) moved to 69

moveLog = []

def log(playerID, tileID, moveType, landlord):
    if moveType == "bought":
        moveLog.append("p" + str(playerID) + " bought " + str(tileID))
    if moveType == "paidRent":
        moveLog.append("p" + str(playerID) + " paid rent to " + str(landlord) + " in " + str(tileID))
    if moveType == "moved":
        moveLog.append("p" + str(playerID) + " moved to " + str(tileID))


#log(1,5,"bought",0)
#log(1,27,"paidRent",3)
#log(1,30,"moved",0)

#print(moveLog)