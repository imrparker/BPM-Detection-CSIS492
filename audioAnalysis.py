# Program: Senior Project
# File: audioAnalysis.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020
# Detect audio peaks with Librosa (https://librosa.github.io/librosa/)

# imports
from __future__ import print_function
import librosa
import numpy as np
import datetime

def startAnalysis():
    print("analysis started")
    y, sr = librosa.load('C:/Users/pkhoc/Desktop/Senior Project/audio files/be.wav')
    duration = librosa.get_duration(y)
    print("File duration(s): ", str(datetime.timedelta(seconds=duration)))
    onset_env = librosa.onset.onset_strength(y=y, sr=sr,
                                             hop_length=512,
                                             aggregate=np.median)
    peaks = librosa.util.peak_pick(onset_env, 3, 3, 3, 5, 0.5, 10)
    print('Peaks detected at: ', librosa.frames_to_time(peaks, sr=sr))
    peak_times = librosa.frames_to_time(peaks, sr=sr)
    #librosa.output.times_csv('./output/peak_times.csv', peak_times)
    #print("Peak times output to ./output/peak_times.csv. \n Process complete.")
