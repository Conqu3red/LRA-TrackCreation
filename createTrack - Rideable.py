import random, math, os, sys
track_name = input("Please enter a track name: ")
name = input("Please enter a save name: ")
name += ".json"
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
file = open(name, "w+")
c = 0
toWrite = ""
toWrite += '{"label": "testData","startZoom": 2,"version": "6.2","startPosition": {"x": 0,"y": -5},"lines": null,"linesArray":['
currentLine = ""
for line in range(number_of_lines):
	currentLine = ""
	currentLine += "["
	c += 1
	currentLine += f"0,"+str(c)+","
	prevx,prevy = x2,y2
	x1,y1,x2,y2 = 0,0,0,0
	x1 += prevx
	x2 += random.randint(int(x1)+minlength,int(x1)+length)
	y1 += prevy
	y2 += random.randint(int(y1-(height/2)),int(y1)+height)

	#print(randnum)
	currentLine += str(x1)+","+str(y1)+","+str(x2)+","+str(y2)+","
	currentLine += "0,false],"
	toWrite += currentLine

toWrite = toWrite[:-1]
toWrite += "]}"

file.write(toWrite)

file.close()

print("Done!")
#read = open(name, "r").read()

#print("File contents: \n\n" + str(read))