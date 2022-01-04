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
    bpmChanges = BPMSTRING.split(",")
    return bpmChanges

# convert our BPM changes located by beats to BPM changes located by ms for use with pydub
#def convertBpmBeatsToMs():
 #   return bpmChangesMs[]

# runtime
# constants:
BPMSTRING = grabBpmChanges()
STARTINGBPM = getStartingBpm(BPMSTRING)
BPMCHANGES = getBpmChanges()

print("This file starts at "+STARTINGBPM+" BPM and has "+str(len(BPMCHANGES))+" changes in BPM")