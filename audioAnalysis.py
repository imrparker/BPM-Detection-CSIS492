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


def startAnalysis():
    print("analysis started")
    y, sr = librosa.load('C:/Users/pkhoc/Desktop/Senior Project/audio files/be.wav')
    duration = librosa.get_duration(y)
    print("File duration(s): ", str(datetime.timedelta(seconds=duration)))
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.median)
    peaks = librosa.util.peak_pick(onset_env, 3, 3, 3, 5, 0.5, 10)
    print('Peaks detected at: ', librosa.frames_to_time(peaks, sr=sr))
    peak_times = librosa.frames_to_time(peaks, sr=sr)


def openAudioSpectrum():
    AudioName = "C:/Users/pkhoc/Desktop/sounds.wav"
    fs, Audiodata = wavfile.read(AudioName)

    plt.plot(Audiodata)
    plt.title("Audio signal in time", size=8)

    plt.show()
