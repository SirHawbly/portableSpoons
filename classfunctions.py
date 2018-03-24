# ------------------------------------------------------------------------------
# Perceptron Class Functions
# ------------------------------------------------------------------------------


def PgetInput(self, inputset):

    pprint(inputset)

    if inputset in record["input"]:
      testInput(inputset)
      return record[inputset]

    else:
      record["input"][size] = {inputset}
      output = decideOutput()
      record["output"][size] = {output}
      size += 1

# ------------------------------------------------------------------------------


def PtestInput(self, inputset):
  pprint(inputset)
  raise NotImplementedError


# ------------------------------------------------------------------------------


def PtestInput(self, inputset):
    pprint(inputset)
    raise NotImplementedError


# ------------------------------------------------------------------------------


def PcheckRecord(self):
  pprint("checking record...")
  raise NotImplementedError


# ------------------------------------------------------------------------------


def PgetOutput(self):
  pprint("getting an output...")
  raise NotImplementedError

  return True


# ------------------------------------------------------------------------------
# General Functions
# ------------------------------------------------------------------------------

VERBOSE = True

# defines the base printing function for this file,
# if the VERBOSE variable is true, it will print things 
# through out the file
def vprint(string):
  if VERBOSE :
    print (string)


# ------------------------------------------------------------------------------
