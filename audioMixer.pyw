from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import os
from pathlib import Path
from pygame import mixer
from threading import Thread
from time import sleep

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

dir = fd.askdirectory(initialdir=os.path.normpath(Path(__file__).parent / "Sounds"), title="Example")
musRaw = os.listdir(dir)
folder = os.path.basename(dir)
print(musRaw)
print(folder)

mus = list()
mus.extend([os.path.splitext(file)[0] for file in musRaw])
print(mus)

S1Int = DoubleVar()
S2Int = DoubleVar()
S3Int = DoubleVar()
S4Int = DoubleVar()
S5Int = DoubleVar()
S6Int = DoubleVar()

root.title("Audio Mixer: "+folder)
ttk.Label(frm, text=folder, font=("Times New Roman", 18), wraplength=300).grid(sticky="w", )


ttk.Label(frm, text=mus[0]).grid(sticky="w", column=0, row=1)
ttk.Scale(frm, value=0, variable=S1Int, from_=0, to=1).grid(sticky="w", column=1 , row=1)

ttk.Label(frm, text=mus[1]).grid(sticky="w", column=0, row=2)
ttk.Scale(frm, value=0, variable=S2Int, from_=0, to=1).grid(sticky="w", column=1, row=2)

ttk.Label(frm, text=mus[2]).grid(sticky="w", column=0, row=3)
ttk.Scale(frm, value=0, variable=S3Int, from_=0, to=1).grid(sticky="w", column=1, row=3)

ttk.Label(frm, text=mus[3]).grid(sticky="w", column=0, row=4)
ttk.Scale(frm, value=0, variable=S4Int, from_=0, to=1).grid(sticky="w", column=1, row=4)

ttk.Label(frm, text=mus[4]).grid(sticky="w", column=0, row=5)
ttk.Scale(frm, value=0, variable=S5Int, from_=0, to=1).grid(sticky="w", column=1, row=5)

ttk.Label(frm, text=mus[5]).grid(sticky="w", column=0, row=6)
ttk.Scale(frm, value=0, variable=S6Int, from_=0, to=1).grid(sticky="w", column=1, row=6)

ScaleVal = Label(root)
ScaleVal.grid()

mixer.init()

a1Note = mixer.Sound(dir+"/"+musRaw[0])
a2Note = mixer.Sound(dir+"/"+musRaw[1])
a3Note = mixer.Sound(dir+"/"+musRaw[2])
a4Note = mixer.Sound(dir+"/"+musRaw[3])
a5Note = mixer.Sound(dir+"/"+musRaw[4])
a6Note = mixer.Sound(dir+"/"+musRaw[5])

mixer.set_num_channels(50)

def QuitProgram():
    global audioLoopRunning
    audioLoopRunning = False
    for i in range(6):
        mixer.Channel(i).stop()
    exit()
tracksPlaying = 0
def checkPlayback():
    for i in range(6):
        global tracksPlaying
        #print(mixer.Channel(i).get_busy())
        #print(i)
        if mixer.Channel(i).get_busy() == True:
            tracksPlaying += 1
            #print(" is busy")
            #print(tracksPlaying)
            #print(" ")

quitButton = ttk.Button(frm, text="Quit", command=QuitProgram).grid()

def audioLoop():
    global audioLoopRunning
    audioLoopRunning = True
    while audioLoopRunning == True:
        a1Note.set_volume(S1Int.get())
        a2Note.set_volume(S2Int.get())
        a3Note.set_volume(S3Int.get())
        a4Note.set_volume(S4Int.get())
        a5Note.set_volume(S5Int.get())
        a6Note.set_volume(S6Int.get())
        global tracksPlaying
        checkPlayback()
        #print(tracksPlaying)
        if tracksPlaying == 0:
            print("LOOP NOW!!! ")
            #print(tracksPlaying)
            for i in range(6):
                mixer.Channel(0).play(a1Note)
                mixer.Channel(1).play(a2Note)
                mixer.Channel(2).play(a3Note)
                mixer.Channel(3).play(a4Note)
                mixer.Channel(4).play(a5Note)
                mixer.Channel(5).play(a6Note)
        tracksPlaying = 0
        sleep(0.01)
        
quitButton
t = Thread(target=audioLoop)
t.start()
root.protocol("WM_DELETE_WINDOW", QuitProgram)
root.mainloop()