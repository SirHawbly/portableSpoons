#!/usr/bin/env python


"""
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
"""


# ------------------------------------------------------------------------------
# Packages 
# ------------------------------------------------------------------------------


import notes


# ------------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------------


overTheRainbow = [['R',00, 1,1],                                                
            # 2nd meter
            ['R',00, 1,1],                                                     
            # 3rd meter
            ['D',-1, 1,2], ['D',00, 1,2],                                     
            # 4th meter
            ['C',00, 1,4], ['A',00, 1,8], ['B',00, 1,8],                       
            ['C',00, 1,4], ['D',00, 1,4],                                      
            # 5th meter
            ['D',-1, 1,2], ['B',00, 1,2],                                      
            # 6th meter
            ['A',00, 3,4], ['R',00, 1,4]]


hotcrossBuns = [['B',00, 1,4],['A',00, 1,4],['G',-1, 1,4],['R',00, 1,4],
            ['B',00, 1,4],['A',00, 1,4],['G',-1, 1,4],['R',00, 1,4],
            ['G',-1, 1,8],['G',-1, 1,8],['G',-1, 1,8],['G',-1, 1,8],
            ['A',00, 1,8],['A',00, 1,8],['A',00, 1,8],['A',00, 1,8],
            ['B',00, 1,4],['A',00, 1,4],['G',-1, 1,4],['R',00, 1,4]]


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


# populates a list of notes that contains the 
# first 6 measures of over the rainbow
def convertNotes(song) :

  time  = 0
  ns    = []

  notes.vprint("")
  notes.vprint("adding a octave, and duration to every note...")
  for i in song :

      #               makeNote(note, octave, length, volume, time) 
      #                        note  octv  length                  vol  time
      ns.append([notes.makeNote(i[0], i[1], int( 16 * i[2] / i[3]), 100, time)])
      time += int(16 * i[2] / i[3])

  # printing all notes in the song
  for n in ns :
    notes.vprint(n)

  notes.vprint("done with converting")
  notes.vprint("")

  return ns


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
  list1.append([GsMajor[n - 1], octave, 1, 4])

notes.vprint("printing the notes in list1")
notes.vprint(list1)
notes.vprint("")

# convert the list of notes to give them a duration and 
# a octave and a note all in a list.
testSong = convertNotes(list1)

notes.vprint("")
notes.vprint("writing notes to MIDI file")
notes.writeToMidi("melody1.mid", 60, testSong)

# print completion message
notes.vprint("done with midi.py")
notes.vprint("")

# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------




