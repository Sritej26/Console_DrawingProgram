class Canvas(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.x1, self.y1, self.x2, self.y2  = 1, 1, w, h
        self.canvasArray = [[' '] * self.w for i in range(self.h)]
        self.canvasObjects = []

    @staticmethod
    def getInstance():
        return Canvas._instance

    def addToCanvas(self, geometryObject):
        self.canvasObjects.append(geometryObject)
        return self.canvasObjects

    def printc(self):
        for o in self.canvasObjects:
            o.drawToCanvas()

        print('-' * (self.w + 2))
        for i in range(self.h):
            tempRow = '|'
            for j in range(self.w):
                tempRow += self.canvasArray[i][j]
            tempRow += '|'
            print(tempRow)
        print('-' * (self.w + 2))

    def erase(self):
        self.canvasArray = [[' '] * self.w for i in range(self.h)]
