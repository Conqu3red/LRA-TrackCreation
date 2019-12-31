class Line:
        def __init__(self,colour,identity,x1,y1,x2,y2):
                self.id = identity
                self.type = colour
                self.x1 = x1
                self.y1 = y1
                self.x2 = x2
                self.y2 = y2

        def getLine(self,identifier):
                self.id = identifier
                return vars(self)
