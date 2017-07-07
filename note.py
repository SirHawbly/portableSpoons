

chain = ""
newLink  = ""

tempNote = None
possibleNotes = []

for note in ('A', 'B', 'C', 'D', 'E', 'F', 'G'):

  ## the notes that dont have flats are c, and f.
  # if (not (note == "C" or note == "F")):
    # tempNote = note + str("b")
    # print(tempNote)

  ## add and print the note
  possibleNotes += [note]
  print (note)

  ## the notes that dont have sharps are b, and e.
  if (not (note == 'B' or note == 'E')):
    tempNote = note + '#'
    possibleNotes += [tempNote]
    print(tempNote)


print(possibleNotes)



data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

print data['name']
