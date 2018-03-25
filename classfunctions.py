"""
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
"""

# This file stores all functions that are needed in side of the classes in 
# classes.py.  This is the .c file to the .h of classes.py.

# ------------------------------------------------------------------------------
# Packages
# ------------------------------------------------------------------------------


# imports


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


def PcheckRecord(self):
  pprint("checking record...")
  raise NotImplementedError


# ------------------------------------------------------------------------------


def PgetOutput(self):
  pprint("getting an output...")
  raise NotImplementedError

  return True


# ------------------------------------------------------------------------------


# connect node to self's input/weight, 
# and the nodes output to self.
def pconnectNodes (self, node, weight):

  # add the new node to the selfs input
  self.nodes['input']  += [node.name]
  self.nodes['weight'] += [weight]

  # add the self to the nodes output
  node.nodes['output'] += [self.name]


# ------------------------------------------------------------------------------
# General Functions
# ------------------------------------------------------------------------------


def testConnect() :

  vprint("\nconnecting 4 to 3 and 4 to 5")
  pnodelist[4].connectNodes(pnodelist[3])
  pnodelist[4].connectNodes(pnodelist[5])

  vprint("3 - " + str(pnodelist[3].nodes))
  vprint("4 - " + str(pnodelist[4].nodes))
  vprint("5 - " + str(pnodelist[5].nodes))


# ------------------------------------------------------------------------------
