from GeometryType.GeometryObject import GeometryObject


class Line(GeometryObject):

    def __init__(self, x1, y1, x2, y2, penStyle = 'x'):
        GeometryObject.__init__(self, 'L', penStyle)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def drawToCanvas(self):
        for i in range(self.canvas.h):
            for j in range(self.canvas.w):
                if i in range(min([self.y1, self.y2])-1, max([self.y1, self.y2])) and \
                        j in range(min([self.x1, self.x2])-1, max([self.x1, self.x2])):
                            self.canvas.canvasArray[i][j] = self.penStyle

    def checkGeometryObjectConstraints(self):
        if (self.x1 < 0) or (self.x2 < 0) or (self.y1 < 0) or (self.y2 < 0):
            print('x and y values need be larger than zero')
            return False

        if min(self.x1, self.x2) < min(self.canvas.x1, self.canvas.x2):
            print('x value is smaller than canvas')
            return False

        if max(self.x1, self.x2) > max(self.canvas.x1, self.canvas.x2):
            print('x value is larger than canvas')
            return False

        if min(self.y1, self.y2) < min(self.canvas.y1, self.canvas.y2):
            print('y value is smaller than canvas')
            return False

        if max(self.y1, self.y2) > max(self.canvas.y1, self.canvas.y2):
            print('y value is larger than canvas')
            return False

        if (self.x1 != self.x2) and (self.y1 != self.y2):
            print('Only horizontal or vertical lines are possible')
            return False

        return True
