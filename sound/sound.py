#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sound.py

Function to play a numpy array as a sound (without using sounddevice).

Before using, install playsound:
    conda install conda-forge::playsound

Created on Tue Sep 24 11:55:05 2024
@author: djangraw
Updated 9/9/25 by DJ - converted to int16 format, normalized amplitude, added default fs.
"""

import numpy as np
from scipy.io import wavfile 
from playsound import playsound

def play(x,fs=44100):
    """
    play a numpy array as a sound.

    Parameters
    ----------
    x : array of floats of size sample_count
        array to play as a sound
    fs : float (optional)
        sampling rate at which to play the sound. The default is 44100.

    Returns
    -------
    None. Saves a file TEMP.wav in the current directory.

    """
    temp_file = 'TEMP.wav'
    # rescale the array so we can cast it to type int16
    amplitude = np.iinfo(np.int16).max
    x = x/np.abs(x).max()*amplitude
    x = x.astype(np.int16)
    # write to file
    wavfile.write(temp_file,fs,x)
    # play from file
    playsound(temp_file)