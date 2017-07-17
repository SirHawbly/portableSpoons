#!/bin/bash

python makeSong.py $1.mid

timidity $1.mid
