import unittest
import sys
sys.path.append("C:/Users/Sritej. N/Downloads/ConsoleDraw")
from GeometryType.Line import Line
from Canvas import Canvas


class TestLine(unittest.TestCase):

    def setUp(self):
        self.w = 4
        self.h = 3
        self.canvas = Canvas(self.w, self.h)
        self.canvasArray = [[' '] * self.w for i in range(self.h)]

    def test__drawToCanvas(self):
        x1, y1, x2, y2 = 1, 1, 3, 1
        line1 = Line(x1, y1, x2, y2)
        line1.drawToCanvas()

        x1, y1, x2, y2 = 3, 2, 3, 3
        line2 = Line(x1, y1, x2, y2)
        line2.drawToCanvas()

        exp1 = [['x', 'x', 'x', ' '], [' ', ' ', 'x', ' '], [' ', ' ', 'x', ' ']]
        self.assertEqual(exp1, self.canvas.canvasArray)

    def test_checkGeometryObjectConstraints(self):
        x11, y11, x21, y21 = 1, 1, 3, 1
        x12, y12, x22, y22 = 1, 1, 5, 1
        x13, y13, x23, y23 = -1, 1, 3, 1
        x14, y14, x24, y24 = 1, 4, 5, 4
        x15, y15, x25, y25 = 1, -1, 3, -1
        x16, y16, x26, y26 = 1, 2, 3, 3

        line1 = Line(x11, y11, x21, y21)
        line2 = Line(x12, y12, x22, y22)
        line3 = Line(x13, y13, x23, y23)
        line4 = Line(x14, y14, x24, y24)
        line5 = Line(x15, y15, x25, y25)
        line6 = Line(x16, y16, x26, y26)

        self.assertEqual(True, line1.checkGeometryObjectConstraints())
        self.assertEqual(False, line2.checkGeometryObjectConstraints())
        self.assertEqual(False, line3.checkGeometryObjectConstraints())
        self.assertEqual(False, line4.checkGeometryObjectConstraints())
        self.assertEqual(False, line5.checkGeometryObjectConstraints())
        self.assertEqual(False, line6.checkGeometryObjectConstraints())


if __name__ == '__main__':
    unittest.main()
