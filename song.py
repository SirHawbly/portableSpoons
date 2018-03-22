#!/usr/bin/env python3


"""
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
"""


# ------------------------------------------------------------------------------
# Packages 
# ------------------------------------------------------------------------------


# import notes


# ------------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------------

scales = [[0, 2, 2, 1, 2, 2, 2, 1], # Major
          [0, 2, 1, 2, 2, 1, 2, 2], # Minor
          [0, 2, 2, 3, 2], # Major Penta
          [0, 3, 2, 2, 3], # Minor Penta
]
  
chords = [[0, 4, 7], # Major Chord
          [0, ], # Minor Chord
          [0, 4, 7, 11], # Maj7 Chord
          [0, ], # Min7 Chord
          [0, ], # Aug Chord
          [0, ], # Dim Chord
          [0, ], # Sus2 Chord
          [0, ], # Sus4 Chord
          [0, ], # Circle Fifths
]

notechain = []


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


# defines the function that is used to populate the list 
# of all possible notes, and their definitions.  This includes 
# their fourths, fifths, etc.
def getAllPossibleNotes():
  
  possNotes = []
  tempNote = None

  #vprint("")
  vprint("\ngetting all possible notes.")

  ## loop for all notes from A to G, all the ones in the scale.
  for note in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):

    ## add and print the note
    possNotes += [note]
    vprint (str('adding ') + note)

    ## the notes that dont have sharps are b, and e.
    if (not (note == 'B' or note == 'E')):
      tempNote = note + '#'
      possNotes += [tempNote]
      vprint(str('adding ') + tempNote)

  ## possNotes now stores a list of all possible note names
  ## now we need to add in functions to get different notes
  allNotes = []

  ## print that we are done with this function and are 
  ## returning the list of all the notes
  vprint ("returning all possible notes\n")
  #vprint ("")

  ## return allNotes which now has all notes 
  ## we can reach from a given note.
  return  possNotes


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


def gensong() :
  ns = []

  i = random(len(notes.possibleNotes))
  key = notes.possibleNotes[i]

  major = notes.getMajorScale(key, notes.possibleNotes)
  minor = notes.getMinorScale(key, notes.possibleNotes)



  return ns


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------


chain = gensong()
getAllPossibleNotes()

# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
