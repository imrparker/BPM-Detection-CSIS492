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
import tkinter as tk
from tkinter import ttk
import BPMdb
matplotlib.use("TkAgg")

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def startAnalysis(filepath):
    print("analysis started")
    y, sr = librosa.load(filepath)
    duration = librosa.get_duration(y)
    onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.median)
    peaks = librosa.util.peak_pick(onset_env, 3, 3, 3, 5, 0.5, 10)
    startstr = str(datetime.timedelta(seconds=duration))
    number = 0
    if startstr[2:4] != "00":
        number = int(startstr[2:4])

    minutesToSeconds = number * 60
    total = minutesToSeconds + int(startstr[5:7])
    final = total / 60
    estmp = len(librosa.frames_to_time(peaks, sr=sr)) / final
    print(int(estmp))
    # peak_times = librosa.frames_to_time(peaks, sr=sr)
    peakNum = str(len(librosa.frames_to_time(peaks, sr=sr)))
    duration = str(datetime.timedelta(seconds=duration))
    wavResults(filepath, estmp, peakNum, duration)


def openAudioSpectrum(filepath):
    AudioName = filepath
    fs, Audiodata = wavfile.read(AudioName)

    plt.plot(Audiodata)
    plt.title("Audio File (Time)", size=8)

    plt.show()


def donothing():
    print("doing nothing")


def wavResults(filepath, msg, peakNum, duration):
    popup = tk.Tk()
    popup.geometry("500x250")
    popup.wm_title("WAV Results")
    filename = ttk.Label(popup, text="File: " + filepath, font=NORM_FONT)
    filename.pack(side="top", fill="x", pady=10)
    tempo = ttk.Label(popup, text="Estimated Tempo: " + str(msg) + " BPM", font=NORM_FONT)
    tempo.pack(side="top", fill="x", pady=10)
    peaksDetected = ttk.Label(popup, text="Peaks Detected: " + peakNum, font=NORM_FONT)
    peaksDetected.pack(side="top", fill="x", pady=10)
    songDuration = ttk.Label(popup, text="WAV Duration: " + duration, font=NORM_FONT)
    songDuration.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    B2 = ttk.Button(popup, text="Save", command=lambda: BPMdb.WAVInsert(filepath, msg, peakNum, duration))
    B2.pack()
    popup.mainloop()
