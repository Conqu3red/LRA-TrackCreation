import json

class Track:
        def __init__(self):
                self.lines = []
                self.data = {"label":"EXAMPLE",
                        "creator":"EXAMPLE",
                        "description":"EXAMPLE",
                        "duration":0,
                        "version":"6.2",
                        "startPosition":{"x":0,"y":0},
                        "lines":[]}

        def setSpawn(self,x,y):
                self.data["startPosition"]["x"] = x
                self.data["startPosition"]["y"] = y

        def addLine(self,line):
                self.lines.append(line)
                
        def saveTrack(self,name):
                with open(name+".json", "w+") as file:
                        for num,line in enumerate(self.lines):
                                self.data['lines'].append(line.getLine(num))
                        json.dump(self.data,file)


