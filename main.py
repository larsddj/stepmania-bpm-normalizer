from pydub import AudioSegment
#import re

#songLoc = input("please paste the .ogg path:")
smLoc = input("please paste the .sm path:")

smFile = open(smLoc, "r")
bpmString = smFile.read()
start = bpmString.find("#BPMS:") + 6
end = bpmString.find(";", start)
print(bpmString[start:end])


#song = AudioSegment.from_ogg(songLoc)

# grab the starting bpm from the SM file
def getStartingBpm():
    return 0

# grab all the beats where BPM changes occur
#def readBpmChanges():
 #   return bpmChanges[]

# convert our BPM changes located by beats to BPM changes located by ms for use with pydub
#def convertBpmBeatsToMs():
 #   return bpmChangesMs[]

