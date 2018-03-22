#!/usr/bin/env python3


"""
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
"""



# ------------------------------------------------------------------------------
# Execution
# ------------------------------------------------------------------------------


import notes
import midi


# ------------------------------------------------------------------------------
# Execution
# ------------------------------------------------------------------------------


chain    = []
newLink  = []

# call the getAllPossibleNotes function to populate all possible notes
# possibleNotes = getAllPossibleNotes()

# did we get anything in the notes section
# vprint(str("possibleNotes: ") + str(possibleNotes))
# vprint("")

# how to get into the transitions
# vprint (str("testing dict access: ") + str(allTransitions["octave"]))
# vprint("")

# checking the scale functions.
# vprint(getMajorScale('A#', possibleNotes))
# vprint(getMinorScale('F#', possibleNotes))
# vprint("")

#testSong = convertNotes(overTheRainbow)
#note.writeToMidi("overTheRainbow.mid", 60, testSong)

#testSong = convertNotes(hotcrossBuns)
#note.writeToMidi("hotcrossBuns.mid", 30, testSong)

notes.vprint("")
notes.vprint("Starting Midi.py")

# change the verbosity variable
if not (input('Verbose? ')) :
    notes.VERBOSE = False

# testing these random note paths
melody1 = [1,1,4,1]
melody2 = [1,3,4,2,2,5,1,5]
list1 = []

# getting the G sharp Scale to put the path on
GsMajor = notes.getMajorScale("G#", notes.possibleNotes)
notes.vprint(GsMajor)

# play the melody on the scale provided
for n in melody2 :
  if (n == 8) :
    octave = 1
  else : 
    octave = 0
  list1.append([GsMajor[n - 1], octave, .5, 3])

notes.vprint("printing the notes in list1")
notes.vprint(list1)
notes.vprint("")

# convert the list of notes to give them a duration and 
# a octave and a note all in a list.
testSong = midi.convertNotes(list1)

notes.vprint("")
notes.vprint("writing notes to MIDI file")
notes.writeToMidi("melody1.mid", 60, testSong)
notes.vprint("")

# test the halfNote function
print (midi.makeHalfNote(('B', 1)))

# print completion message
notes.vprint("done with midi.py")
notes.vprint("")

# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------


