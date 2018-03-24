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


import random
# import notes

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class perceptron:
  size   = 0
  record = {"input"  : {}, 
            "output" : {}}

  def getInput(inputset):
    vprint(inputset)
    if inputset in record["input"]:
      testInput(inputset)
      return record[]

  def testInput(inputset):
    vprint(inputset)

  def checkRecord():
    vprint("asdf")
  
  def getOutput():
    vprint("asdf")


# ------------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------------

VERBOSE = True

          # 8
scales = {'maj' : [2, 2, 1, 2, 2, 2, 1], # Major
          "min" : [2, 1, 2, 2, 1, 2, 2], # Minor
          # 7
          "dor" : [2, 1, 2, 2, 2, 1, 2], # Dorian
          "dor" : [2, 1, 2, 2, 2, 1, 2], # Dorian
          "mix" : [2, 2, 1, 2, 2, 1, 2], # Mixolydian
          # 6
          "mix" : [1, 2, 1, 1, 1, 2], # Mixolydian
          "mix" : [1, 2, 1, 2, 1, 2], # Mixolydian
          # 5
          "map" : [2, 2, 3, 2], # Major Penta
          "mip" : [3, 2, 2, 3], # Minor Penta
}

chords = {"maj" : [4, 7, 11], # Maj Chord
          "min" : [3, 5, 10], # Min Chord
          "aug" : [4, 8, 11], # Aug Chord
          "dim" : [3, 6,  9], # Dim Chord
          "su2" : [2, 7, 10], # Sus2 Chord
          "su4" : [5, 7, 10], # Sus4 + 7th Chord
          # finish
          # "cir" : [0, ], # Circle Fifths
}

notechain = []


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


# defines the base printing function for this file,
# if the VERBOSE variable is true, it will print things 
# through out the file
def vprint(string):
  if VERBOSE :
    print (string)


# ------------------------------------------------------------------------------


# given a note, its octave, and its length, make a tuple out of it,
# to be used in generating a list (song).
def makeNote (note, octave, length, volume, time) :
  return {
            'note'   : note,
            'octave' : octave,
            'length' : length,
            'volume' : volume,
            'time'   : time,
            # TODO ADD TEMPO AND VOLUME
            # 'tempo'  : tempo,
            # 'volume' : volume,
         }


# ------------------------------------------------------------------------------


# defines the function that is used to populate the list 
# of all possible notes, and their definitions.  This includes 
# their fourths, fifths, etc.
def getAllNotes():
  
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


def getScale(root, scale):
  vprint("\ngetting " + 
          str(allNotes[root]) + 
          " " + 
          str(list(scales)[scale]) + 
          " scale")

  # set up an set with the root inside
  i = 0
  scaleNotes = [allNotes[root]]

  if root <= len(allNotes) :
    i = root
  else :
    print("GETSCALE ERROR: note value '" + 
          str(root) + 
          "' not in possible notes")

  for value in scales[list(scales)[scale]] :
    i += value
    scaleNotes += [allNotes[i % len(allNotes)]]

  return scaleNotes


# ------------------------------------------------------------------------------


# given a list of notes, octaves, and times (A, 1, 1,4) 
# create note objects that can be written to a file.
def convertNotes(song) :

  time  = 0
  ns    = []

  vprint("\nadding a octave, and duration to every note...")
  for i in song :

      #               makeNote(note, octave, length, volume, time) 
      #                         note  octv  length                  vol  time
      ns.append([notes.makeNote(i[0], i[1], int( 16 * i[2] / i[3]), 100, time)])
      time += int(16 * i[2] / i[3])

  # printing all notes in the song
  for n in ns :
    vprint(n)

  vprint("done with converting\n")

  return ns


# ------------------------------------------------------------------------------

def getNotes(scales)

  note = None

  for scale in scales:
    for note in scale:


  return Note

# ------------------------------------------------------------------------------


def gensong() :
  notes = []
  allScales = []
  allScalesNames = []

  for i in range(0, 5) :
    key = random.randrange(len(allNotes))
    scaletype = random.randrange(len(scales))
    
    allScales += [getScale(key, scaletype), ]
    allScalesNames += [[allNotes[key], list(scales)[scaletype]] ,]

    vprint("adding scale...")
    vprint("\t" + str(allScalesNames[i]))
    vprint("\t" + str(allScales[i]))

  notes = getNotes(allScales)

  return notes


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------


allNotes = getAllNotes()

chain = gensong()


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
