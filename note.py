
import copy


VERBOSE = True 

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

  vprint("getting all possible notes.")

  for note in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):

    ## add and print the note
    possNotes += [note]
    vprint (str('adding') + note)

    ## the notes that dont have sharps are b, and e.
    if (not (note == 'B' or note == 'E')):
      tempNote = note + '#'
      possNotes += [tempNote]
      vprint(str('adding') + tempNote)

  ## pNotes now stores a list of all possible note names

  allNotes = []

  return possNotes

# ------------------------------------------------------------------------------

chain = ""

newLink  = ""

tempNote = None

possibleNotes = getNotes()

vprint(possibleNotes)


musicNote = {
   'name' : 'unInit',
   'fourths' : [],
   'fifths' : [],
   'octaves' : [],
   'minorThird' : [],
   'majorThird' : [],
}

vprint(musicNote["name"])


