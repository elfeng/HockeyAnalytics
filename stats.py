import pandas as pd
import numpy as np
import json
import importAndIterate


#get processed json data
breakwayData = importAndIterate.listOfEntries

#dictionary storing success/failure counts of breakaways by player
playerSuccessCountsDump = {}
playerSuccessCountsDrop = {}

#dictionary storing total entry attempts by player
playerAttemptCountsDump = {}
playerAttemptCountsDrop = {}

#iterate through json data looking for different styles, add counts to successCounts
def compareStyle():
    dumpCount = 0
    dropCount = 0
    dumpSuccess = 0
    dropSuccess = 0
    for i in range(0, len(breakwayData)):
        if breakwayData[i].style == "drop":
            dropCount = dropCount + 1
            if breakwayData[i].success == True:
                dropSuccess = dropSuccess + 1
        else:
            dumpCount = dumpCount + 1
            if breakwayData[i].success == True:
                dumpSuccess = dumpSuccess + 1
    print("Dump count: %d \n" % dumpCount)
    print("Drop count: %d \n" % dropCount)
    print("Dump success: %d \n" % dumpSuccess)
    print("Drop success: %d \n" % dropSuccess)

def comparePlayerDrop():
    for i in range(0, len(breakwayData)):
        if breakwayData[i].style == "drop":
            if breakwayData[i].initiating_player in playerAttemptCountsDrop:
                playerAttemptCountsDrop[breakwayData[i].initiating_player] += 1
            else:
                playerAttemptCountsDrop[breakwayData[i].initiating_player] = 1
            if breakwayData[i].success == True:
                if breakwayData[i].initiating_player in playerSuccessCountsDrop:
                    playerSuccessCountsDrop[breakwayData[i].initiating_player] += 1
                else:
                    playerSuccessCountsDrop[breakwayData[i].initiating_player] = 1
    playerSuccessRatesDrop = {}
    for player in playerAttemptCountsDrop:
        if player in playerSuccessCountsDrop:
            playerSuccessRatesDrop[player] = playerSuccessCountsDrop[player] / playerAttemptCountsDrop[player]
        else:
            playerSuccessRatesDrop[player] = 0
    print (playerSuccessRatesDrop)

def comparePlayerDump():
    for i in range(0, len(breakwayData)):
        if breakwayData[i].style == "dump":
            if breakwayData[i].initiating_player in playerAttemptCountsDump:
                playerAttemptCountsDump[breakwayData[i].initiating_player] += 1
            else:
                playerAttemptCountsDump[breakwayData[i].initiating_player] = 1
            if breakwayData[i].success == True:
                if breakwayData[i].initiating_player in playerSuccessCountsDump:
                    playerSuccessCountsDump[breakwayData[i].initiating_player] += 1
                else:
                    playerSuccessCountsDump[breakwayData[i].initiating_player] = 1
    playerSuccessRatesDump = {}
    for player in playerAttemptCountsDump:
        if player in playerSuccessCountsDump:
            playerSuccessRatesDump[player] = playerSuccessCountsDump[player] / playerAttemptCountsDump[player]
        else:
            playerSuccessRatesDump[player] = 0
    print (playerSuccessRatesDump)


compareStyle()
comparePlayerDrop()
comparePlayerDump()
