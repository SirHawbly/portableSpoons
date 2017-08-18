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


import copy
from midiutil.MidiFile import MIDIFile


# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------


# this is the verbosity variable, set
# it to true when you need information.
VERBOSE = True 


# ------------------------------------------------------------------------------


# define a440 
# the note ill center this piece of code on sometime in the future....
a440 = 440


# ------------------------------------------------------------------------------


# defines the variable that will define the notes in a chord
noteType = {
  'note'     : 1, ## most likely for bass?
  'interval' : 2, ## most likely for drums?
  'small'    : 3, ## most likely for lead instruments?
  'medium'   : 4, ## lead?
  'large'    : 5, ## lead?
}


# ------------------------------------------------------------------------------


# defines the variable that will talk about how a 
# chord is composed, TODO
intervalType = {
  'minor'      : 0, ## these will have impact on how dissonant a 
  'major'      : 0, ## song is, with the more dissonant it becomes,
  'augmented'  : 0, ## the more probable the consonance upcoming.
  'diminished' : 0, ##
  'sus2'       : 0, ##
  'sus4'       : 0, ##
}


# ------------------------------------------------------------------------------


# derived from 
#   https://en.wikipedia.org/wiki/Consonance_and_dissonance#Consonance

# these are lists of all the perfect and imperfect consonances 
allConsonances = {
  'perfect'   : ['unisons', 'octaves', 'fourths', 'fifths'],
  'imperfect' : ['majorThirds', 'minorSixths', 'minorThirds', 'majorSixths'],
}


# ------------------------------------------------------------------------------


# derived from
#  http://www2.siba.fi/muste1/index.php?id=65&la=en

# these are lists of all the hard and soft dissonances. 
allDissonances = {
  'sharp' : ['minorSecond', 'majorSeventh'],
  'soft'  : ['majorSeconds', 'minorSeventh', 'tritone'],
}


# ------------------------------------------------------------------------------


# derived from the list of links at 
#   https://en.wikipedia.org/wiki/Consonance_and_dissonance#Consonance

# this dictionary contains all of the ways to reach notes either 
# via semitones or via frequencies, as im not sure which i will be using.
allTransitions = {
  # https://en.wikipedia.org/wiki/Unison
  'unison'      : [[0], [[1/1]]],            ## +00 semis

  # https://en.wikipedia.org/wiki/Major_second
  'minorSecond' : [[1], [[16/15], [17/16]]], ## +01 semis 27/25, 135/128, 25/24

  # https://en.wikipedia.org/wiki/Semitone
  'majorSecond' : [[2], [[9/8], [10/9]]],    ## +02 semis

  # https://en.wikipedia.org/wiki/Minor_third
  'minorThird'  : [[3], [[6/5], [19/16]]],   ## +03 semis

  # https://en.wikipedia.org/wiki/Major_third
  'majorThird'  : [[4], [[5/4]]],            ## +04 semis

  # https://en.wikipedia.org/wiki/Perfect_fourth
  'fourth'      : [[5], [[4/3]]],            ## +05 semis

  # https://en.wikipedia.org/wiki/Tritone
  'tritone'     : [[6], [[25/18], [36/25]]], ## +06 semis 45/32, 64/45, 7/5,...

  # https://en.wikipedia.org/wiki/Perfect_fifth
  'fifth'       : [[7], [[3/2]]],            ## +07 semis

  # https://en.wikipedia.org/wiki/Minor_sixth
  'minorSixth'  : [[8], [[8/5], [11/7]]],    ## +08 semis

  # https://en.wikipedia.org/wiki/Major_sixth
  'majorSixth'  : [[9], [[5/3], [12/7]]],    ## +09 semis

  # https://en.wikipedia.org/wiki/Minor_seventh
  'minorSeventh': [[10], [[16/9], [9/5]]],   ## +10 semis

  # https://en.wikipedia.org/wiki/Major_seventh
  'majorSeventh': [[11], [[15/8], [50/27]]], ## +11 semis

  # https://en.wikipedia.org/wiki/Octave
  'octave'      : [[12], [[2/1]]],           ## +12 semis
}


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


# http://musictheorysite.com/major-scales/
def getMajorScale(root, notes):
  vprint("getting " + str(root) + " major scale")

  # set up an set with the root inside
  i = 0
  scale = [root]

  if root in notes :
      i = notes.index(root)
  else :
      print("ERROR: note " + str(root) + " not in " + str(notes))

  # Major scale formula
  # W - W - H - W - W - W - H
  for value in ['W', 'W', 'H', 'W', 'W', 'W', 'H'] :
    if (value == 'W') :
      i += 2
    else :
      i += 1
    scale += [notes[i % len(notes)]]

  return scale


# ------------------------------------------------------------------------------


# http://musictheorysite.com/minor-scales/
def getMinorScale(root, notes):
  vprint("getting " + str(root) + " minor scale")

  # set up an set with the root inside
  i = 0
  scale = [root]

  if root in notes :
      i = notes.index(root)
  else :
      print("ERROR: note " + str(root) + " not in " + str(notes))

  # Natural Minor Scale Formula
  # W - H - W - W - H - W - W
  for value in ['W', 'H', 'W', 'W', 'H', 'W', 'W'] :
    if (value == 'W') :
      i += 2
    else :
      i += 1
    scale += [notes[i % len(notes)]]

  return scale


# ------------------------------------------------------------------------------


# http://musictheorysite.com/pentatonic-scales/
def getMajorPentaScale(root, notes):
  vprint("getting " + str(root) + " majpenta scale")

  i = 0
  scale = [root]
  
  if root in notes :
      i = notes.index(root)
  else :
      print("ERROR: note " + str(root) + " not in " + str(notes))

  # Get the notes 1, 2, 3, 5, 6.  Remove the 4th and 7th.
  for value in [2, 2, 3, 2] : 
    i += value
    scale += [notes[i % len(notes)]]
    

  return scale


# ------------------------------------------------------------------------------


# http://musictheorysite.com/pentatonic-scales/
def getMinorPentaScale(root, notes):
  vprint("getting " + str(root) + " minpenta scale")

  i = 0
  scale = [root]
  
  if root in notes :
      i = notes.index(root)
  else :
      print("ERROR: note " + str(root) + " not in " + str(notes))

  # Get the notes 1, 3, 4, 5, 7. Remove the 2nd and 6th,
  for value in [3, 2, 2, 3] : 
    i += value
    scale += [notes[i % len(notes)]]

  return scale
 

# ------------------------------------------------------------------------------


# http://musictheorysite.com/the-circle-of-fifths/
def getCircleOfFifths():
  # TODO
  print("setting up the scale of fifths")
  

# ------------------------------------------------------------------------------

def getMajor(root, notes):
  print("getting a " + str(root) +  " major chord")

  # get the root, the major third and the perf fifth,
  # maybe a seventh or ninth as well.

  i = 0
  chord = [root]

  if root in notes :
    i = notes.index(root)
  else :
    print("ERROR: note " + str(root) + " not in " + str(notes))

  for note in ['majorThird', 'fifth', 'majorSeventh'] :
    j = (allTransitions[note])[0]
    chord += notes[(i+j[0]) % len(notes)]

  return chord

# ------------------------------------------------------------------------------


def getMinor(root, notes):
  # TODO
  print("getting a minor")

  # get the root, the minor third and the perf fifth,
  # maybe a seventh or ninth as well.

# ------------------------------------------------------------------------------


def getAugmented(root):
  # TODO
  print("getting a aug")

  # get a root, a major third, and a augmented fifth,
  # (raise the perf fifth a half step).


# ------------------------------------------------------------------------------


def getDiminished(root):
  # TODO
  print("getting a dim")

  # get a root, a minor third, and a diminished fifth,
  # (lower the perf fifth a half step).
  

# ------------------------------------------------------------------------------


def getSus2(root):
  # TODO
  print("getting a sus2")

  # get a root, a major second, and a perf fifth,
  

# ------------------------------------------------------------------------------


def getSus4(root):
  # TODO
  print("getting a sus4")

  # get a root, a perf fourth, and a perf fifth,
  

# ------------------------------------------------------------------------------


# defines the function that is used to populate the list 
# of all possible notes, and their definitions.  This includes 
# their fourths, fifths, etc.
def getAllPossibleNotes():
  
  possNotes = []
  tempNote = None

  vprint("")
  vprint("getting all possible notes.")

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

  # for note in possNotes :
    # vprint (note)


  ## print that we are done with this function and are 
  ## returning the list of all the notes
  vprint ("returning all possible notes")
  vprint ("")

  ## return allNotes which now has all notes 
  ## we can reach from a given note.
  return  possNotes


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


# given a note and octave, turn that into a midi pitch
def MIDIpitch(note, octave) :

  # midi middle C (C4)
  pitch = 60

  # get from C to A, (C -> B -> Bb -> A)
  pitch = pitch - 3

  # take off or add 12 to pitch per octave
  pitch = pitch + (12 * octave)

  # add on pitch per location in possible notes 
  pitch = pitch + possibleNotes.index(note)

  # print out the results
  vprint(str(note) + ":" + str(octave) + " -> " + str(pitch))

  return pitch


# ------------------------------------------------------------------------------


# given a string of notes, their intervals and their sequence,
# output them to a midifile, of a given name.
def writeToMidi(title, tempo, notes) :

  # open up the media file.
  mf = MIDIFile(1, adjust_origin=1)

  track    = 0
  time     = 0.0
  temptime = 0
  channel  = 0
  volume   = 100

  # initialize the first track.
  mf.addTrackName(track, time, title)
  mf.addTempo(track, time, tempo * 16)

  # notes should be a list of lists, with notes in the 
  # sub lists occuring at the same time.
  for chord in notes :
    for sound in chord :

      # save the time interval for the notes.  
      # they should all be the same within the chord.

      # vprint(sound)

      # temptime = sound["time"]

      # add the note to the midi track if its not a rest
      if (sound['note'] != 'R') :
        mf.addNote(track, channel, MIDIpitch(sound['note'], sound['octave']), \
                sound['time'], sound['length'], sound['volume'])

    # increase the time counter
    # time += temptime

  with open(title, 'wb') as outf:
    mf.writeFile(outf)


# ------------------------------------------------------------------------------
# New Variables
# ------------------------------------------------------------------------------


# need this for later, function was jsut defined
possibleNotes = getAllPossibleNotes()


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
