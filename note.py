

# ------------------------------------------------------------------------------
# Packages 
# ------------------------------------------------------------------------------


import copy


# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------


## this is the verbosity variable, set
## it to true when you need information.
VERBOSE = True 


## define a440 
## the note ill center this pieceof code on
a440 = 440


# ------------------------------------------------------------------------------


## defines the variable that will define the notes in a chord
noteType = {
  'note'     : 1, ## most likely for bass?
  'interval' : 2, ## most likely for drums?
  'small'    : 3, ## most likely for lead instruments?
  'medium'   : 4, ## lead?
  'large'    : 5, ## lead?
}


# ------------------------------------------------------------------------------


## defines the variable that will talk about how a 
## chord is composed, TODO
intervalType = {
  'minor'      : 0, ## these will have impact on how dissonant a 
  'major'      : 0, ## song is, with the more dissonant it becomes,
  'augmented'  : 0, ## the more probable the consonance upcoming.
  'diminished' : 0, ## 
}


# ------------------------------------------------------------------------------


## derived from 
##   https://en.wikipedia.org/wiki/Consonance_and_dissonance#Consonance

## these are lists of all the perfect and imperfect consonances 
allConsonances = {
  'perfect'   : ['unisons', 'octaves', 'fourths', 'fifths'],
  'imperfect' : ['majorThirds', 'minorSixths', 'minorThirds', 'majorSixths'],
}


# ------------------------------------------------------------------------------


## derived from
##  http://www2.siba.fi/muste1/index.php?id=65&la=en

## these are lists of all the hard and soft dissonances. 
allDissonances = {
  'sharp' : ['minorSecond', 'majorSeventh'],
  'soft'  : ['majorSeconds', 'minorSeventh', 'tritone'],
}


# ------------------------------------------------------------------------------


## derived from the list of links at 
##   https://en.wikipedia.org/wiki/Consonance_and_dissonance#Consonance

## this dictionary contains all of the ways to reach notes either 
## via semitones or via frequencies, as im not sure which i will be using.
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


# defines the function that is used to populate the list 
# of all possible notes, and their definitions.  This includes 
# their fourths, fifths, etc.
def getNotes():
  
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
# Execution
# ------------------------------------------------------------------------------


chain = ""
newLink  = ""

# call the getNotes function to populate all possible notes
possibleNotes = getNotes()

# did we get anything in the notes section
vprint(str("possibleNotes: ") + str(possibleNotes))
vprint("")

# how to get into the transitions
vprint (str("testing dict access: ") + str(allTransitions["octave"]))
vprint("")

# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
