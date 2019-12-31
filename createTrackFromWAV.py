import random, math, os, sys



"""
IMPORTANT
json format (per line)
[l_type, id, x1, y1, x2, y2, 0, false]
l_type - line type (0=normal, 1=red, 2=green)
id - unique line identefier
x, y - coords of line points [line joins from point (x1,y1) to (x2,y2)]

Co-ordinate grid:
            y-
            |
            |
            |
            |
x- ---------+--------- x+   x axis
            |
            |
            |
            |
            y+
          y axis



Speeds - red
line len | speed (p/f)
100         5.95
200         8.62
300        10.57
400        12.25
500        13.73
1000       19.51
"""
path = input("Please enter the path of your wav file: ")
import soundfile as sf
data, samplerate = sf.read(path)
channels = 2
try:
	print(len(data[0]))
except:
	channels = 1
	pass
#print(channels)
track_name = input("Please enter a track name: ")
name = input("Please enter a save name: ")
name += ".json"
#number_of_lines = int(input("Enter the number of lines to be Created: "))
#minlength = int(input("Enter minimum line length: "))
#length = int(input("Enter maximum line length: "))
#height = int(int(input("Enter maximum line height: "))/2)
try:
    # Create target Directory
    os.mkdir(track_name)
except FileExistsError:
    pass
#print(data[0])
os.chdir(track_name)
if channels == 1:
	x1,y1,x2,y2 = 0,0,0,(data[0])*200
elif channels == 2:
	x1,y1,x2,y2 = 0,0,0,(data[0][0])*200
file = open(name, "w+")
toWrite = ""
toWrite += '{"label": "testData","startZoom": 1.4,"version": "6.2","startPosition": {"x": -6700,"y": -5},"lines": null,"linesArray":['
currentLine = ""
for c,line in enumerate(data):
	currentLine = ""
	currentLine += "["
	#c += 1
	currentLine += f"2,"+str(c)+","
	prevx,prevy = x2,y2
	x1,y1,x2,y2 = 0,0,0,0
	x1 += prevx
	x2 += c
	y1 += prevy
	if channels == 1:
		y2 += line*200
	elif channels == 2:
		y2 += ((line[0]+line[1])/2)*200

	#print(randnum)
	currentLine += str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","
	currentLine += "0,false],"
	toWrite += currentLine
toWrite += "[0,"+str(len(data))+"0,0,0,"+str(len(data))+",0,false],"
toWrite += "[1,"+str(len(data)+1)+",-6700,0,0,0,0,false]"

#toWrite = toWrite[:-1]
toWrite += "]}"

file.write(toWrite)

file.close()

print("Done!")
#read = open(name, "r").read()

#print("File contents: \n\n" + str(read))