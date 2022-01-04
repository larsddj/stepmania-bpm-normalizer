from os import replace
from pydub import AudioSegment
import shutil
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
    beat = -1.0
    bpm = -1.0
    ms = -1.0

    def __init__(self, beat, bpm):
        self.beat = beat
        self.bpm = bpm

    def getBpm(self):
        return self.bpm 

    def setMs(self, ms):
        self.ms = ms

# convert our BPM changes located by beats to BPM changes located by ms for use with pydub
# you use a calc of 60,000 / BPM to get the amount of ms per beat
# if you have the ms per beat you can see at what ms bpmchanges occur
# ! BE CAREFUL, YOU NEED TO TRACK CUMULATIVE BEATS BECAUSE OF CHANGES IN BPM AFFECTING REAL TIME MS !

def convertBpmBeatsToMs(bpmChangesObj):
    currentMsPerBeat = 0
    previousMsPerBeat = 0
    previousBeat = 0
    beatDifference = 0
    msDifference = 0
    cumulativeMs = 0


    for bpmChange in bpmChangesObj:
        print("Previous Beat: "+str(previousBeat))
        # at first we calculate a ms per beat at the current bpm 
        currentMsPerBeat = 60000 / float(bpmChange.getBpm())
        print("Current MS for a Beat: "+str(currentMsPerBeat))
        print("Current BPM: "+ bpmChange.getBpm())
        # then we calculate the amount of beats passed since the previous bpm change
        beatDifference = float(bpmChange.beat) - previousBeat
        print("Current Beat: "+str(bpmChange.beat))
        print("Beats passed since previous change: "+str(beatDifference))
        # from that we can calculate the time in ms that has passed
        msDifference = beatDifference*previousMsPerBeat
        print("MS passed since previous change: "+str(msDifference))
        # finally we have a cumulative ms that ends up being the timestamp of the bpm change
        cumulativeMs+= msDifference
        print("Cumulative MS passed: "+str(cumulativeMs))
        print("------------------------------------------------------------")

        # at last we set the timestamp to the bpm change object
        bpmChange.setMs(cumulativeMs) 
        previousBeat = float(bpmChange.beat)
        previousMsPerBeat = currentMsPerBeat
    
    return bpmChange

# def makeNormalizedSmFile():
#     # copy over the file (probably breaks on other operating systems oops)
#     originalSm = r'fractal/fractal.sm'
#     newSm = r'fractal_new.sm'
#     shutil.copyfile(originalSm, newSm)

#     # grab and replace the bpm text
#     newSmFile = open("fractal_new.sm", "r")
#     bpmString = newSmFile.read()
#     start = bpmString.find("#BPMS:") + 6
#     end = bpmString.find(";", start)
#     bpmString = bpmString[start:end]

    #with open('fractal_new.sm', 'w') as file:
     #   file.write(filedata)

# runtime
# constants:
BPM_STRING = grabBpmChanges()
STARTING_BPM = getStartingBpm(BPM_STRING)
BPM_CHANGES_STRING_LIST = getBpmChanges()
BPM_CHANGES_OBJ = getBpmChangeListObj(BPM_CHANGES_STRING_LIST)
convertBpmBeatsToMs(BPM_CHANGES_OBJ)

print("This file starts at "+STARTING_BPM+" BPM and has "+str(len(BPM_CHANGES_STRING_LIST))+" changes in BPM")

# for ch in BPM_CHANGES_OBJ:
#     print(str(ch.beat) + "=" + str(ch.bpm) + "=" + str(ch.ms))