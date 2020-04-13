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
import midi
from mido import MidiFile

matplotlib.use("TkAgg")
NORM_FONT = ("Helvetica", 10)


def startWAVAnalysis(filepath):
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


def startMIDIAnalysis(filepath):
    metaList = []

    mid = MidiFile(filepath, clip=True)
    for x in mid.tracks[0]:
        metaList.append(x)

    strList = str(metaList[4])
    if strList[36] == " ":
        strList = strList[30:36]
    elif strList[36] == "t":
        strList = strList[30:35]

    intTempo = (int(strList) / 600000) * 100
    print(str(intTempo))

    midiResults(filepath, str(intTempo))


def openAudioSpectrum(filepath):
    AudioName = filepath
    fs, Audiodata = wavfile.read(AudioName)

    plt.plot(Audiodata)
    plt.title("Audio File (Time)", size=8)

    plt.show()


def openMidiSpectrum(filepath):
    song = midi.read_midifile(filepath)
    song.make_ticks_abs()
    tracks = []
    for track in song:
        notes = [note for note in track if note.name == 'Note On']
        pitch = [note.pitch for note in notes]
        tick = [note.tick for note in notes]
        tracks += [tick, pitch]
    plt.plot(*tracks)
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
    B2 = ttk.Button(popup, text="Show Audio Spectrum", command=lambda: openAudioSpectrum(filepath))
    B2.pack()
    popup.mainloop()


def midiResults(filepath, msg):
    popup = tk.Tk()
    popup.geometry("500x250")
    popup.wm_title("MIDI Results")
    filename = ttk.Label(popup, text="File: " + filepath, font=NORM_FONT)
    filename.pack(side="top", fill="x", pady=10)
    tempo = ttk.Label(popup, text="Estimated Tempo: " + str(msg) + " BPM", font=NORM_FONT)
    tempo.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()
    B2 = ttk.Button(popup, text="Save", command=lambda: BPMdb.MIDIInsert(filepath, msg))
    B2.pack()
    B2 = ttk.Button(popup, text="Show Audio Spectrum", command=lambda: openMidiSpectrum(filepath))
    B2.pack()
    popup.mainloop()
