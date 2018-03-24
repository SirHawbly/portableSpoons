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

import classfunctions 
from random import randrange


# ------------------------------------------------------------------------------
# Song Variables
# ------------------------------------------------------------------------------


              # 8
allScales = {"maj" : [2, 2, 1, 2, 2, 2, 1], # Major
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

allChords = {"maj" : [4, 7, 11], # Maj Chord
              "min" : [3, 5, 10], # Min Chord
              "aug" : [4, 8, 11], # Aug Chord
              "dim" : [3, 6,  9], # Dim Chord
              "su2" : [2, 7, 10], # Sus2 + 7th Chord
              "su4" : [5, 7, 10], # Sus4 + 7th Chord
              # finish
              # "cir" : [0, ], # Circle Fifths
              }

allNotes = []

noteChain = []


# ------------------------------------------------------------------------------
# Setup Funtions
# ------------------------------------------------------------------------------


# defines the function that is used to populate the list 
# of all possible notes, and their definitions.  This includes 
# their fourths, fifths, etc.
def getAllNotes():
  
  possNotes = []
  tempNote = None

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

  ## print that we are done with this function and are 
  ## returning the list of all the notes
  vprint ("returning all possible notes\n")

  ## return allNotes which now has all notes 
  ## we can reach from a given note.
  allNotes = possNotes


# ------------------------------------------------------------------------------


def getScale(root, scale):
  vprint("\ngetting " + 
          str(allNotes[root]) + 
          " " + 
          str(list(allScales)[scale]) + 
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

  for value in list(allScales)[list(scales)[scale]] :
    i += value
    scaleNotes += [allNotes[i % len(allNotes)]]

  return scaleNotes


# ------------------------------------------------------------------------------


def getNote(scales):

  note = None

  i = randrange(len(allScales))
  j = randrange(len(allScales)[i])

  return allScales[i][j]


# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class perceptron:
  size   = 0
  record = {"input"  : {}, 
            "output" : {}}

  VERBOSE = True

  def pprint(self, string):
    if VERBOSE:
      print(str(string))

perceptron.getInput = classfunctions.PgetInput
perceptron.testInput = classfunctions.PtestInput
perceptron.checkRecord = classfunctions.PcheckRecord
perceptron.getOutput = classfunctions.PgetOutput


# ------------------------------------------------------------------------------
# Song Functions
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