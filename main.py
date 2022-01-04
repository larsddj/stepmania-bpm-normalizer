from pydub import AudioSegment
#import re

#songLoc = input("please paste the .ogg path:")
smLoc = input("please paste the .sm path:")
desiredBpm = input("please entire the desired BPM to normalize to: ")

def grabBpmChanges():
    smFile = open(smLoc, "r")
    bpmString = smFile.read()
    start = bpmString.find("#BPMS:") + 6
    end = bpmString.find(";", start)
    bpmString = bpmString[start:end]
    return bpmString


#song = AudioSegment.from_ogg(songLoc)

# grab the starting bpm from the SM file
def getStartingBpm(bpmString):
    start = bpmString.find("0=") + 2
    end = bpmString.find(",", start)
    startingBpm = bpmString[start:end]
    return startingBpm

# grab all the beats where BPM changes occur
def getBpmChanges():
    bpmChanges = BPM_STRING.split(",")
    return bpmChanges

def getBpmChangeListObj(bpmChangesString):
    bpmObj = []
    for bpm in bpmChangesString:
        splitStr = bpm.split('=')
        curBeat = splitStr[0]
        curBpm = splitStr[1]

        bpmObj.append(bpmChange(curBeat, curBpm))
    
    return bpmObj

class bpmChange():
    beat = -1
    bpm = -1
    ms = -1

    def __init__(self, beat, bpm):
        self.beat = beat
        self.bpm = bpm

# convert our BPM changes located by beats to BPM changes located by ms for use with pydub
# you use a calc of 60,000 / BPM to get the amount of ms per beat
# if you have the ms per beat you can see at what ms bpmchanges occur
# ! BE CAREFUL, YOU NEED TO TRACK CUMULATIVE BECAUSE OF CHANGES !

def convertBpmBeatsToMs(bpmChangesObj):
    curMs = 0
    cumMs = 0
    curMsPerBeat = 0

    for bpmChange in bpmChangesObj:
        curMsPerBeat = 60000 / bpmChange.bpm
        cumMs = curMs + cumMs
        curMs =  bpmChange.beat * curMsPerBeat

# runtime
# constants:
BPM_STRING = grabBpmChanges()
STARTING_BPM = getStartingBpm(BPM_STRING)
BPM_CHANGES_STRING = getBpmChanges()

print("This file starts at "+STARTING_BPM+" BPM and has "+str(len(BPM_CHANGES_STRING))+" changes in BPM")