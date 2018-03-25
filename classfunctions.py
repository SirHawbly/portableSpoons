"""
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
"""


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


def pconnectNodes (self, node):

  # add the new node to the selfs output
  self.nodes[1] += [node.name]
  # add the self to the nodes input
  node.nodes[0] += [self.name]


# ------------------------------------------------------------------------------
# General Functions
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------


def testConnect() :

  vprint("\nconnecting 4 to 3 and 4 to 5")
  pnodelist[4].connectNodes(pnodelist[3])
  pnodelist[4].connectNodes(pnodelist[5])

  vprint("3 - " + str(pnodelist[3].nodes))
  vprint("4 - " + str(pnodelist[4].nodes))
  vprint("5 - " + str(pnodelist[5].nodes))


# ------------------------------------------------------------------------------
