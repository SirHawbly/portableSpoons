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


import notes
import wav


# ------------------------------------------------------------------------------
# Variables
# ------------------------------------------------------------------------------


# the lowest we can hear is at 20Hz, so we will save this value
# this will define the scale of the frequency map.
lowestFrequency = 20


# ------------------------------------------------------------------------------


# this is the highest frequency, 20,000Hz this will also influence
# the frequency map.
highestFrequency = 20000 


# ------------------------------------------------------------------------------


# this is the variable that defines the slices in 
# the array that will determine the frequency
segments = 12


# ------------------------------------------------------------------------------


# this variable stores the number of octaves we can
# go either down or up, for a given note. 
octaves = 3


# ------------------------------------------------------------------------------


# this is the list of floats that will determine the 
# range and volumes of the tones that will play at 
# any one time.
blankArray = []

# create a 2d array of values with dimensions 
# [octaves*2 + 1, segments]
for i in range(-octaves, octaves) :
  temp = []
  for i in range(0, segments) :
    temp.append([])
  blankArray.append(temp)

# notes.vprint(blankArray) 


# ------------------------------------------------------------------------------
# Functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# Execution
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------




