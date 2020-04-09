# Program: Senior Project
# File: userInterface.py
# Author: Parker Ostertag
# CSIS 492 Spring 2020

import audioAnalysis
from tkinter import *
from tkinter import filedialog


def createUI():
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

    # Placeholder Function
    def doNothing():
        print("Doing nothing")

    # FILE BROWSER
    def fileBrowser():
        # This program can only analyse .wav files at the moment... I think
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("wav files", "*.wav"), ("all files", "*.*")))

    def audioAnalysisWindow():
        newroot = Tk()
        newroot.title("Audio Analysis")
        # newroot.mainloop()
        audioAnalysis.startAnalysis()

    # ROOT
    root = Tk()
    root.title("Audio Tempo Analysis - Parker Ostertag")
    menu = Menu(root)
    root.config(menu=menu)

    # toolbar = Frame(root, bg = "orange")
    toolbar = Frame(root)

    # MIDI TEMPO ANALYSIS
    button1 = Button(toolbar, text="MIDI Tempo Analysis", command=doNothing, height=30, width=50, bg="#C2C2C2")
    button1.pack(side=LEFT, padx=10, pady=20)
    toolbar.pack(side=TOP, fill=X)

    button2 = Button(toolbar, text="WAV Tempo Analysis", command=fileBrowser, height=30, width=50, bg="#C2C2C2")
    button2.pack(side=RIGHT, padx=10, pady=20)

    # FRAME
    frame = Frame(root, width=600, height=0)
    frame.pack()

    # FILE MENU
    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New Audio File...", command=fileBrowser)
    subMenu.add_command(label="New...", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Exit", command=root.destroy)

    # EDIT MENU
    editMenu = Menu(menu)
    menu.add_cascade(label="Edit", menu=editMenu)
    editMenu.add_command(label="Redo", command=doNothing)
    editMenu.add_command(label="Undo", command=doNothing)

    root.mainloop()
