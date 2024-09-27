#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example script that can be used to test sound.py and its play() function.

Created on Tue Sep 24 12:00:40 2024
@author: djangraw
"""

import numpy as np
from sound import play

# generate a tone (sine wave)
fs = 44100 # sampling frequency in Hz
t = np.arange(0,1,1/fs) # time array
f = 440 # middle C
x = np.sin(2*np.pi*f*t) # sine wave

# Use sound.play to play the sound, saving a TEMP.wav file in the process
play(x,fs)
