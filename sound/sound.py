#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sound.py

Function to play a numpy array as a sound (without using sounddevice).

Before using, install playsound:
    conda install conda-forge::playsound

Created on Tue Sep 24 11:55:05 2024

@author: djangraw
"""

from scipy.io import wavfile 
from playsound import playsound

def play(x,fs):
    """
    play a numpy array as a sound.

    Parameters
    ----------
    x : array of floats of size sample_count
        array to play as a sound
    fs : float
        sampling rate at which to play the sound

    Returns
    -------
    None. Saves a file TEMP.wav in the current directory.

    """
    temp_file = 'TEMP.wav'
    wavfile.write(temp_file,fs,x)
    playsound(temp_file)