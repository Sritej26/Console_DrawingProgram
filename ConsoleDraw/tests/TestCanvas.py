import unittest
import sys
sys.path.append("C:/Users/Sritej. N/Downloads/ConsoleDraw")
from Canvas import Canvas
from GeometryType.Line import Line


class TestCanvas(unittest.TestCase):

    def setUp(self):
        self.w = 4
        self.h = 3
        self.canvas = Canvas(self.w, self.h)
        self.testCanvasArray = [[' '] * self.w for i in range(self.h)]


    def test_createCanvas(self):
        self.assertEqual(self.w, self.canvas.w)
        self.assertEqual(self.h, self.canvas.h)
        self.assertEqual(self.testCanvasArray, self.canvas.canvasArray)
        self.assertEqual([], self.canvas.canvasObjects)

    def test_erase(self):
        x1, y1, x2, y2 = 1, 1, 3, 1
        line = Line(x1, y1, x2, y2)
        line.drawToCanvas()
        test = [['x', 'x', 'x', ' '], [' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ']]
        self.assertEqual(test, self.canvas.canvasArray)
        self.canvas.erase()
        self.assertEqual(self.testCanvasArray, self.canvas.canvasArray)

    def test_addToCanvas(self):
        x1, y1, x2, y2 = 1, 1, 3, 1
        line = Line(x1, y1, x2, y2, penStyle='x')
        self.assertEqual(0, len(self.canvas.canvasObjects))
        self.canvas.addToCanvas(line)
        self.assertEqual(1, len(self.canvas.canvasObjects))


if __name__ == '__main__':
    unittest.main()
