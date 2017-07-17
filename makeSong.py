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


import note


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

            # 1st meter
  for i in song :

      # makeNote (note, octave, length, volume, time) 
      #                          note  octv  length                  vol  time
      ns.append([note.makeNote(i[0], i[1], int( 16 * i[2] / i[3]), 100, time)])
      time += int(16 * i[2] / i[3])

  # printing all notes in the song
  for n in ns :
    note.vprint(n)

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

testSong = convertNotes(overTheRainbow)
note.writeToMidi("overTheRainbow.mid", 60, testSong)

testSong = convertNotes(hotcrossBuns)
note.writeToMidi("hotcrossBuns.mid", 30, testSong)


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------




