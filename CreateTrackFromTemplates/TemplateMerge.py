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

def getStartEnd(lines):
	start_line = [0,0,1000000,100000000,10000000000,100000000]
	for line in lines:
		if line[2] < start_line[2]:
			start_line = line

	end_line = [0,0,0,0,0,0]
	for line in lines:
		if line[4] > end_line[4]:
			end_line = line
	return [[start_line[2],start_line[3]],[end_line[4],end_line[5]]]

def translate(line,x,y):
	line[2] += x
	line[4] += x
	line[3] += y
	line[5] += y
	return line
#print(getStartEnd(templates[1]))

# TODO
#   FIX IDs of the lines so they all render
mainTrack = Track()
tracks = {}
start = (0,0)
end = (0,0)
lines_added = 0
this_loop_lines = []
iterations = int(input("Enter the number of templates to be joined: "))
for i in range(iterations):
	choice = random.choice(list(templates.keys()))
	print("Chosen "+str(choice))
	#print(choice)
	if i == 0:
		startend = getStartEnd(templates[choice]["linesArray"])
	else:
		startend = getStartEnd(this_loop_lines)
	#print(startend)
	for num,line in enumerate(templates[choice]["linesArray"]):
		if num == 0:
			startend[0][0] = line[2]
			startend[0][1] = line[3]
		print(line)
		x_shift = max(startend[0][0],end[0]) - min(startend[0][0],end[0])
		y_shift = max(startend[0][1],end[1]) - min(startend[0][1],end[1])
		print(x_shift, y_shift)
		line = translate(line,x_shift,y_shift)
		print(line)
		lines_added += 1
		line[1] = lines_added
		mainTrack.addLine(Line(*line))
		this_loop_lines.append(line)
	end = getStartEnd(this_loop_lines)
	end = (end[1][0],end[1][1])
	print("END: "+ str(end))
os.chdir(tracks_dir)
track_name = input("Enter a track name: ")
name = input("Enter a save name: ")
try:
	# Create target Directory
	os.mkdir(track_name)
except FileExistsError:
	pass
os.chdir(track_name)
mainTrack.saveTrack(name)
#print(templates)







#print(templates[1])
#print(translate(templates[1]))
#track = Track()
#for line in templates[1]["linesArray"]:
#	track.addLine(Line(*line))
#track.translate(20,0)
#track.saveTrack(name)

#print("Done")