<!---
  * Copyright (c) 2017 Christopher Bartlett
  * [This program is licensed under the "GPL License"]
  * Please see the file LICENSE in the source
  * distribution of this software for license terms.
-->

# portableSpoons - Programatic Music Generator

Copyright (c) 2017 Christopher Bartlett

A music generation tool written in Python.  This software was written to help me understand different sections of programming.  When fully developed, this software will be a Python script that uses a neural network to output a working script that can be used in SuperCollider, an open source music tool written in Python.  It will also have some ability to output to a midi file for quick playback.


# Status

Right now, This software is in the beggining stages of development.  The features that have been completed are outputting to midi, and creating some test songs that are pre-written.  Some of the next things that need to be implemented are outputting to something SuperCollider can parse, stringing notes together in a nice way, and creating multiple parts/instruments for a song.

More information about the Status of the project can be found in the todo.txt file.


# Usage

To start off, you will need to clone this repo.  

In order to run the files in this project, you will need some specific tools:  
  . Python  
  . Midiutil (a python library)  
  . A Midi Player (I use Timidity on linux)   
  . A Wav Player  
  . and eventually SuperCollider  
  
Right now, the code for testing Midi output is ran in the midi.py file.  This will most likely be shifted into the createSong.sh script at a later date.

You can make two test midi files by running :
 `python midi.py`

More features will be implemented as the project goes on.


# License

This program is licensed under the GPL version 3 or later. Please check the LICENSE file for specific information about licensing terms



