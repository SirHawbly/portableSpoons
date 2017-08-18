#!/usr/bin/env python

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

# ------------------------------------------------------------------------------
# Execution 
# ------------------------------------------------------------------------------



notes.vprint ("")
notes.vprint ("testing scales in notes.py")
notes.vprint (notes.getMajor('C', notes.possibleNotes))

notes.vprint ("")
notes.vprint (notes.getMajorPentaScale('C', notes.possibleNotes))

notes.vprint ("")
notes.vprint (notes.getMinorPentaScale('E', notes.possibleNotes))

notes.vprint ("done with scales")
notes.vprint ("")


# ------------------------------------------------------------------------------
# End
# ------------------------------------------------------------------------------
