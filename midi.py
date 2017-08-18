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


# given a note and octave, add (1,4) to the end
# for use in creating writable notes.
def makeQuarterNote(note) :
  if (len(note) == 2) :
    notes.vprint("hey this is a good note.")
    return note + (1,4)
  else :
    notes.vprint("ERROR: note had too many fields")


# ------------------------------------------------------------------------------


# given a note and octave, add (1,2) to the end
# for use in creating writable notes.
def makeHalfNote(note) :
  if (len(note) == 2) :
    notes.vprint("hey this is a good note.")
    return note + (1,2)
  else :
    notes.vprint("ERROR: note had too many fields")


# ------------------------------------------------------------------------------


# given a list of notes, octaves, and times (A, 1, 1,4) 
# create note objects that can be written to a file.
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
# End
# ------------------------------------------------------------------------------
