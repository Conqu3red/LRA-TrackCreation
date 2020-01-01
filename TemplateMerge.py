import random, math, os, sys, json, tkinter
from track import *
from line import *
from tkinter import *
from tkinter.filedialog import askdirectory
#with open('settings.conf') as config:
#    data = json.load(config)



tk=Tk()
tracks_dir = askdirectory(title='Please select the location of your LRA tracks folder')

tk.destroy()
os.chdir("Templates")
templates = {}
for filename in os.listdir():
	if filename.endswith(".json"):
		with open(filename) as json_file:
			data = json.load(json_file)
			templates[int(filename[:-5])] = data
	else:
		continue
os.chdir(tracks_dir)
track_name = input("Enter a track name: ")
name = input("Enter a save name: ")
try:
    # Create target Directory
    os.mkdir(track_name)
except FileExistsError:
    pass

#print(templates)

os.chdir(track_name)
start_line = [0,0,1000000,100000000,10000000000,100000000]
for line in templates[1]["linesArray"]:
	if line[2] < start_line[0]:
		start_line = line
#print(start_line)
end_line = [0,0,0,0,0,0]
for line in templates[1]["linesArray"]:
	if line[4] > end_line[4]:
		end_line = line
#print(start_line, end_line)
#print(templates[1])
#print(translate(templates[1]))
track = Track()
for line in templates[1]["linesArray"]:
	track.addLine(Line(*line))
track.translate(20,0)
track.saveTrack(name)

print("Done")