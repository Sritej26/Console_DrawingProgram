from GeometryType.GeometryObject import GeometryObject
from GeometryType.Line import Line


class Rectangle(GeometryObject):

    def __init__(self, x1, y1, x2, y2, penStyle = 'x'):
        GeometryObject.__init__(self, 'R', penStyle)
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def drawToCanvas(self):
        line1 = Line(self.x1, self.y1, self.x2, self.y1)
        line2 = Line(self.x1, self.y2, self.x2, self.y2)
        line3 = Line(self.x1, self.y1, self.x1, self.y2)
        line4 = Line(self.x2, self.y1, self.x2, self.y2)

        line1.drawToCanvas()
        line2.drawToCanvas()
        line3.drawToCanvas()
        line4.drawToCanvas()


    def checkGeometryObjectConstraints(self):
        if self.x1 > self.x2 or self.y1 > self.y2:
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

        return True
