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
# Functions
# ------------------------------------------------------------------------------


VERBOSE = True

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
# Main
# ------------------------------------------------------------------------------





# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
