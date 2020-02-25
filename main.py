# Program: Senior Project
# Author: Parker Ostertag
# CSIS 492 Spring 2020
import wave
from tkinter import *
from tkinter import filedialog


def main():
    createUI()


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

    def audioAnalysis():
        newroot = Tk()
        newroot.title("Audio Analysis")
        newroot.mainloop()

    # ROOT
    root = Tk()
    root.title("Audio Tempo Analysis - Parker Ostertag")
    menu = Menu(root)
    root.config(menu=menu)

    #toolbar = Frame(root, bg = "orange")
    toolbar = Frame(root)
    button1 = Button(toolbar, text = "button1", command = audioAnalysis)
    button1.pack(side = LEFT, padx = 2, pady = 20)
    toolbar.pack(side = TOP, fill = X)

    # FRAME
    frame = Frame(root, width=900, height=550)
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


if __name__ == "__main__":
    main()
