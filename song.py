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


from network import getNoteIndex
from network import allScales
from network import getScale
from network import vprint

from midiutil.MidiFile import MIDIFile

# from copy import deepcopy


# ------------------------------------------------------------------------------
# Song Variables
# ------------------------------------------------------------------------------


CHANNELS = 10

VERBOSE = True


# ------------------------------------------------------------------------------
# Song Functions
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
  notes    = []

  vprint("\nadding a octave, and duration to every note...")

  for i in song :
      #               makeNote(note, octave, length, volume, time) 
      #                         note  octv  length                  vol  time
      notes.append([makeNote(i[0], i[1], int( 16 * i[2] / i[3]), 100, time)])
      time += int(16 * i[2] / i[3])

  # printing all notes in the song
  for note in notes :
    vprint(note)

  vprint("done with converting\n")
  return notes


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
  pitch = pitch + getNoteIndex(note)

  # print out the results
  vprint(str(note) + ":\t" + str(octave) + " -> " + str(pitch))

  return pitch


# ------------------------------------------------------------------------------


# given a string of notes, their intervals and their sequence,
# output them to a midifile, of a given name.
def writeToMidi(title, tempo, notes) :

  # open up the media file.
  mf = MIDIFile(CHANNELS, adjust_origin=1)

  track    = 0
  time     = 0.0
  temptime = 0
  channel  = 0
  volume   = 100

  # initialize the first track.
  mf.addTrackName(track, time, title)
  mf.addTempo(track, time, tempo * 12)

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
        mf.addNote(track, 
                   channel, 
                   MIDIpitch(sound['note'], 
                   sound['octave']), 
                   sound['time'], 
                   sound['length'], 
                   sound['volume'])

    # increase the time counter
    # time += temptime

  with open(title, 'wb') as outf:
    mf.writeFile(outf)


# ------------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------------


if not (input('\nVerbose? ')) :
    VERBOSE = False

# testing these random note paths
melody1 = [1,1,4,1]
melody2 = [1,3,4,2,2,5,1,5]
list1 = []

l = list(allScales.keys())

# getting the G sharp Scale to put the path on
GsMajor = getScale(8, "maj")
vprint(GsMajor)

# play the melody on the scale provided
for n in melody2 :
  if (n == 8) :
    octave = 1
  else : 
    octave = 0
  list1.append([GsMajor[n - 1], octave, .5, 3])

vprint("\nprinting the notes in list1")
vprint(list1)

# convert the list of notes to give them a duration and 
# a octave and a note all in a list.
testSong = convertNotes(list1)

vprint("writing notes to MIDI file")
writeToMidi("melody2.mid", 60, testSong)

# print completion message
vprint("done with midi.py")


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
