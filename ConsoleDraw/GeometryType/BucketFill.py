from GeometryType.GeometryObject import GeometryObject


class BucketFill(GeometryObject):

    def __init__(self, x, y, penStyle = 'x'):
        GeometryObject.__init__(self, 'B', penStyle)
        self.x = x
        self.y = y

    def drawToCanvas(self):

        if self.canvas.x1 <= self.x <= self.canvas.x2 and self.canvas.y1 <= self.y <= self.canvas.y2 and self.canvas.canvasArray[self.y - 1][self.x - 1] == ' ':
            self.canvas.canvasArray[self.y - 1][self.x - 1] = str(self.penStyle)
            b1 = BucketFill(self.x, self.y + 1, self.penStyle)
            b1.drawToCanvas()
            b2 = BucketFill(self.x, self.y - 1, self.penStyle)
            b2.drawToCanvas()
            b3 = BucketFill(self.x + 1, self.y, self.penStyle)
            b3.drawToCanvas()
            b4 = BucketFill(self.x - 1, self.y, self.penStyle)
            b4.drawToCanvas()

    def checkGeometryObjectConstraints(self):
        if self.x < min(self.canvas.x1, self.canvas.x2):
            print('x value is smaller than canvas')
            return False

        if self.x > max(self.canvas.x1, self.canvas.x2):
            print('x value is larger than canvas')
            return False

        if self.y < min(self.canvas.y1, self.canvas.y2):
            print('y value is smaller than canvas')
            return False

        if self.y > max(self.canvas.y1, self.canvas.y2):
            print('y value is larger than canvas')
            return False

        return True