import classfunctions

# ------------------------------------------------------------------------------
# Classes
# ------------------------------------------------------------------------------


class perceptron:
  # member variables
  name    = 0
  size    = 0
  record  = {"input"  : {}, 
             "output" : {}}
  nodes   = [[], []] # nodes that point to [0] and point from here [1]
  VERBOSE = True

  # print function
  def pprint(self, string):
    if self.VERBOSE:
      print("\tperceptron: " + str(string))

  def __init__(self, pname=0, precord = None, psize = None, pnodes = [[], []]):
    if pname : self.name = pname
    if psize : self.size = psize
    if precord : self.record = precord
    if pnodes : self.nodes = pnodes
    self.pprint("newNode '" + str(self.name) + "'")

# add functions that are in the class functions file
perceptron.getInput = classfunctions.PgetInput
perceptron.testInput = classfunctions.PtestInput
perceptron.checkRecord = classfunctions.PcheckRecord
perceptron.getOutput = classfunctions.PgetOutput
perceptron.connectNodes = classfunctions.pconnectNodes
