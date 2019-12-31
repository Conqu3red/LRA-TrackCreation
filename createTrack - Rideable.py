import random, math, os, sys, json, tkinter
from track import *
from line import *
from tkinter import *
from tkinter.filedialog import askdirectory
#with open('settings.conf') as config:
#    data = json.load(config)
config = open("settings.conf", "r")
config_data = config.read()
#print(config_data)
config.close()
tk=Tk()
tracks_dir = askdirectory(title='Please select the location of your LRA tracks folder')
tk.destroy()
os.chdir(tracks_dir)

track_name = input("Please enter a track name: ")
name = input("Please enter a save name: ")
number_of_lines = int(input("Enter the number of lines to be Created: "))
minlength = int(input("Enter minimum line length: "))
length = int(input("Enter maximum line length: "))
height = int(int(input("Enter maximum line height: "))/2)
try:
    # Create target Directory
    os.mkdir(track_name)
except FileExistsError:
    pass

os.chdir(track_name)
x1,y1,x2,y2 = 0,0,0,0
identity = 0
track = Track()
track.setSpawn(0,-5)
for line in range(number_of_lines):
	identity += 1
	prevx,prevy = x2,y2
	x1,y1,x2,y2 = 0,0,0,0
	x1 += prevx
	x2 += random.randint(int(x1)+minlength,int(x1)+length)
	y1 += prevy
	y2 += random.randint(int(y1-(height/2)),int(y1)+height)
	track.addLine(Line(0,identity,x1,y1,x2,y2))
	#print(randnum)

track.saveTrack(name)
print("Done!")
#read = open(name, "r").read()

#print("File contents: \n\n" + str(read))
