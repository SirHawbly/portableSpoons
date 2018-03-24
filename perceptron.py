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
# Print Functions
# ------------------------------------------------------------------------------


VERBOSE = True

# defines the base printing function for this file,
# if the VERBOSE variable is true, it will print things 
# through out the file
def vprint(string):
  if VERBOSE :
    print (string)


# ------------------------------------------------------------------------------
# Song Variables
# ------------------------------------------------------------------------------

# the relative relationships between notes in a scale
noteRelations = {
  # allConsonants 
  'perfect'   : [0, 7, 12], # unison, 5th, octave
  'imperfect' : [3, 4, 8, 9], # maj3rd, min3rd, maj6th, min6th
  # allDissonances
  'soft' : [2, 5, 11, 13], # maj2nd, min7th, maj9th
  'sharp'  : [1, 6, 10, 14], # min2nd, tritone, maj7th, min9th
}

              # 8
allScales = { "maj" : [2, 2, 1, 2, 2, 2, 1], # Major
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

allChords = { "maj" : [4, 7, 11], # Maj Chord
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
    #vprint (str('adding ') + note)

    ## the notes that dont have sharps are b, and e.
    if (not (note == 'B' or note == 'E')):
      tempNote = note + '#'
      possNotes += [tempNote]

  ## print that we are done with this function and are 
  ## returning the list of all the notes
  vprint ("returning all possible notes")

  ## return allNotes which now has all notes 
  ## we can reach from a given note.
  return possNotes
  

# ------------------------------------------------------------------------------


def getNoteIndex(note):
  return allNotes.index(note)


# ------------------------------------------------------------------------------


# given an offset for the allNotes list,
# and a scale key for the allScales list
# output all the notes in that scale
def getScale(rootIndex, scaleIndex):

  vprint("getting " + str(allNotes[rootIndex]) +
          " " + str(scaleIndex) + " scale")

  scale = [allNotes[rootIndex], ]
  i = rootIndex

  for dist in allScales[scaleIndex]:
    i += dist
    scale += [allNotes[i % len(allNotes)]]

  return scale


# ------------------------------------------------------------------------------


def getNote(scales, i, j):

  if  not (i and j):
    i = randrange(len(allScales))
    j = randrange(len(allScales)[i])

  return allScales[i][j]


# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class perceptron:
  # member variables
  name = 0
  size   = 0
  record = {"input"  : {}, 
            "output" : {}}
  nodes = [[], []]
  VERBOSE = True

  # print function
  def pprint(self, string):
    if self.VERBOSE:
      print("\tperceptron: " + str(string))

  def __init__(self, pname=0, precord = None, psize = None, pnodes = [[], []]):
    self.name = pname
    self.size = psize
    self.record = precord
    self.nodes = pnodes
    self.pprint("newNode '" + str(self.name) + "'")

# add functions that are in the class functions file
perceptron.getInput = classfunctions.PgetInput
perceptron.testInput = classfunctions.PtestInput
perceptron.checkRecord = classfunctions.PcheckRecord
perceptron.getOutput = classfunctions.PgetOutput


# ------------------------------------------------------------------------------
# Song Functions
# ------------------------------------------------------------------------------


def gensong() :
  notes = []
  Scales = []
  ScaleNames = []

  vprint(len(allNotes))
  vprint(len(allScales))

  for i in range(0, 5) :
    key = randrange(len(allNotes))
    scaleType = randrange(len(allScales))
    
    Scales += [getScale(key, scaleType), ]
    ScaleNames += [[allNotes[key], list(allScales)[scaleType]] ,]

    vprint("adding scale...")
    vprint("\t" + str(ScaleNames[i]))
    vprint("\t" + str(Scales[i]))

  notes = getNotes(allScales)

  return notes


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------


allNotes = getAllNotes()

#gensong()

p = perceptron(pname=100)


# ------------------------------------------------------------------------------

