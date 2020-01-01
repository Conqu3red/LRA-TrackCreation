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
length = len(os.listdir())
for filename in os.listdir():
	if filename.endswith(".json"):
		with open(filename) as json_file:
			data = json.load(json_file)
			templates[int(filename[:-5])] = data
	else:
		continue

def getStartEnd(temp):
	start_line = [0,0,1000000,100000000,10000000000,100000000]
	for line in temp["linesArray"]:
		if line[2] < start_line[0]:
			start_line = line

	end_line = [0,0,0,0,0,0]
	for line in temp["linesArray"]:
		if line[4] > end_line[4]:
			end_line = line
	return [(start_line[2],start_line[3]),(end_line[4],end_line[5])]

#print(getStartEnd(templates[1]))

# TODO
#   FIX IDs of the lines so they all render
mainTrack = Track()
tracks = {}
start = (0,0)
end = (0,0)
for i in range(3):
	tracks[i] = Track()
	num = random.randint(1,2)
	startEnd = getStartEnd(templates[num])
	print("Chosen "+str(num))
	for num,line in enumerate(templates[num]["linesArray"]):
		tracks[i].addLine(Line(*line))
		mainTrack.addLine(Line(*line))
	tracks[i].saveTrack(str(i))
	
	x_shift = max(startEnd[0][0],end[0]) - min(startEnd[0][0],end[0])
	y_shift = max(startEnd[0][1],end[1]) - min(startEnd[1][1],end[1])
	print(x_shift, y_shift)
	tracks[i].translate(x_shift, y_shift)
	end = (startEnd[1][0],startEnd[1][1])
	#for num,line in enumerate(tracks[i].lines):
	#	mainTrack.addLine(*list(tracks[i].getLine(num).values()))

os.chdir(tracks_dir)
track_name = input("Enter a track name: ")
name = input("Enter a save name: ")
try:
    # Create target Directory
    os.mkdir(track_name)
except FileExistsError:
    pass
mainTrack.saveTrack(name)
#print(templates)

os.chdir(track_name)





#print(templates[1])
#print(translate(templates[1]))
#track = Track()
#for line in templates[1]["linesArray"]:
#	track.addLine(Line(*line))
#track.translate(20,0)
#track.saveTrack(name)

#print("Done")