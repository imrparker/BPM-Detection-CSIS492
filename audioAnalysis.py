# Program: Senior Project
# File: audioAnalysis.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020

# imports
from __future__ import print_function
import librosa
import datetime
import matplotlib
from scipy.io import wavfile
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use("TkAgg")


def startAnalysis(filepath):
    print("analysis started")
    y, sr = librosa.load(filepath)
    duration = librosa.get_duration(y)
    print("File duration(s): ", str(datetime.timedelta(seconds=duration)))
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.median)
    peaks = librosa.util.peak_pick(onset_env, 3, 3, 3, 5, 0.5, 10)
    print('Peaks detected at: ', librosa.frames_to_time(peaks, sr=sr))
    #print((len(librosa.frames_to_time(peaks, sr=sr) / 60 )))
    startstr = str(datetime.timedelta(seconds=duration))
    number = 0
    if startstr[2:4] != "00":
        number = int(startstr[2:4])

    minutesToSeconds = number * 60
    final = minutesToSeconds + int(startstr[5:7])
    print((len(librosa.frames_to_time(peaks, sr=sr) / final)))
    peak_times = librosa.frames_to_time(peaks, sr=sr)


def openAudioSpectrum(filepath):
    AudioName = filepath
    fs, Audiodata = wavfile.read(AudioName)

    plt.plot(Audiodata)
    plt.title("Audio File (Time)", size=8)

    plt.show()
