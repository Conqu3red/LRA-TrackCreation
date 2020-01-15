import random, math, os, sys, json, tkinter
from track import *
from line import *
from tkinter import *
from tkinter.filedialog import askdirectory
#with open('settings.conf') as config:
#    data = json.load(config)

y_increase = 0
y_decrease = 0
tk=Tk()
tracks_dir = askdirectory(title='Please select the location of your LRA tracks folder')
tk.destroy()
os.chdir(tracks_dir)

track_name = input("TRACK NAME  Please enter a track name: ")
name = input("NAME  Please enter a save name: ")
number_of_lines = int(input("NUMBER_OF_LINES  Enter the number of lines to be Created: "))
minlength = int(input("MINLENGTH  Enter minimum line length: "))
length = int(input("LENGTH  Enter maximum line length: "))
y_increase = int(input("Y_INCREASE  Enter the maximum y drop (line going down): ")) # For more selection about valid random lines
y_decrease = int(input("Y_DECREASE  Enter the maximum y increase (line going up): ")) # For more selection about valid random lines
# NOTE on y_increase and y_decrease
# 		- y_increase should usually be 2x y_decrease to ensure an incline downhill

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
	y2 += random.randint(int(y1-y_decrease),int(y1)+y_increase)
	track.addLine(Line(0,identity,x1,y1,x2,y2,0,False))
	#print(randnum)

track.saveTrack(name)
print("Done!")
#read = open(name, "r").read()

#print("File contents: \n\n" + str(read))
