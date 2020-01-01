import json, math
from line import *

class Track:
        def __init__(self):
                self.lines = []
                self.data = {"label":"EXAMPLE",
                        "creator":"EXAMPLE",
                        "description":"EXAMPLE",
                        "duration":0,
                        "version":"6.2",
                        "startPosition":{"x":0,"y":0},
                        "lines":[],
                        "linesArray":[]}

        def setSpawn(self,x,y):
                self.data["startPosition"]["x"] = x
                self.data["startPosition"]["y"] = y

        def addLine(self,line):
                self.lines.append(line)

        def translate(self,x_shift,y_shift):
                done = 0
                needed = len(self.lines)
                for num,line in enumerate(self.lines):
                        self.lines.remove(line)
                        current = list(line.getLine(num).values())
                        print(current)
                        current[2],current[4] = math.floor(current[2])+x_shift, math.floor(current[4])+x_shift
                        current[3],current[5] = math.floor(current[3])+y_shift, math.floor(current[5])+y_shift
                        current = list(current)
                        print(current)
                        #print(current)
                        self.lines.append(Line(*current))
                        done += 1
                        
                        if done == needed:
                                print("Break")
                                break

        def saveTrack(self,name):
                with open(name+".json", "w+") as file:
                        for num,line in enumerate(self.lines):
                                self.data['linesArray'].append(list(line.getLine(num).values()))
                        json.dump(self.data,file)


