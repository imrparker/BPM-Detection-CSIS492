# Program: Senior Project
# File: userInterface.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020

import audioAnalysis
from tkinter import *
from tkinter import filedialog, ttk
import tkinter as tk
import BPMdb


def dbFail(msg):
    popup = tk.Tk()
    popup.geometry("350x100")
    popup.wm_title("Conn Failed")
    label = ttk.Label(popup, text=msg)
    label.pack(side=TOP)
    B1 = ttk.Button(popup, text="Darn", command=popup.destroy)
    B1.pack()


def dbSuccess(msg):
    popup = tk.Tk()
    popup.geometry("350x100")
    popup.wm_title("Conn Success")
    label = ttk.Label(popup, text=msg)
    label.pack(side=TOP)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


def dbDroppedRecords():
    popup = tk.Tk()
    popup.geometry("350x100")
    popup.wm_title("Deletion Success")
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


def dbSaveSuccess():
    popup = tk.Tk()
    popup.geometry("350x100")
    popup.wm_title("Success")
    label = ttk.Label(popup, text="Saved To Database")
    label.pack(side=TOP)
    B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


def createUI():
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

    # Placeholder Function
    def doNothing():
        print("Doing nothing")

    # FILE BROWSERS
    def WAVfileBrowser():
        # This program can only analyse .wav files at the moment... I think
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("wav files", "*.wav"), ("all files", "*.*")))

        if root.filename == '':
            return 1

        audioAnalysis.startWAVAnalysis(root.filename)
        # audioAnalysis.openAudioSpectrum(root.filename)

    def MIDIfileBrowser():
        # This program can only analyse .MID files
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("mid files", "*.mid"), ("all files", "*.*")))

        if root.filename == '':
            return 1

        audioAnalysis.startMIDIAnalysis(root.filename)

    def audioAnalysisWindow():
        newroot = Tk()
        newroot.title("Audio Analysis")
        # newroot.mainloop()
        audioAnalysis.startWAVAnalysis()

    def dbSettings():
        popup = tk.Tk()
        popup.geometry("600x480")
        popup.wm_title("Database Settings")
        B1 = ttk.Button(popup, text="Test Database Connection", command=BPMdb.testConnection)
        B1.pack()
        B2 = ttk.Button(popup, text="Delete All WAV Records", command=BPMdb.WAVDropRecords)
        B2.pack()
        B3 = ttk.Button(popup, text="Delete All MIDI Records", command=BPMdb.MIDIDropRecords)
        B3.pack()

    # ROOT
    root = Tk()
    root.title("Audio Tempo Analysis - Parker Ostertag")
    menu = Menu(root)
    root.config(menu=menu)

    # toolbar = Frame(root, bg = "orange")
    toolbar = Frame(root)

    # MIDI TEMPO ANALYSIS
    button1 = Button(toolbar, text="MIDI Tempo Analysis", command=MIDIfileBrowser, height=30, width=50, bg="#C2C2C2")
    button1.pack(side=LEFT, padx=10, pady=20)
    toolbar.pack(side=TOP, fill=X)

    button2 = Button(toolbar, text="WAV Tempo Analysis", command=WAVfileBrowser, height=30, width=50, bg="#C2C2C2")
    button2.pack(side=RIGHT, padx=10, pady=20)

    # FRAME
    frame = Frame(root, width=600, height=0)
    frame.pack()

    # FILE MENU
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Audio File...", command=WAVfileBrowser)
    subMenu.add_command(label="New...", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=root.destroy)

    # EDIT MENU
    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)
    editMenu.add_command(label="Undo", command=doNothing)

    # SETTINGS MENU
    settingsMenu = Menu(menu)
    menu.add_cascade(label="Settings", menu=settingsMenu)
    settingsMenu.add_command(label="Database Settings", command=dbSettings)

    root.mainloop()
