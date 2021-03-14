import unittest
import sys
sys.path.append("C:/Users/Sritej. N/Downloads/ConsoleDraw")
from Canvas import Canvas
from GeometryType.Rectangle import Rectangle


class TestRectangel(unittest.TestCase):

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test__drawToCanvas(self):
        x1, y1, x2, y2 = 1, 1, 3, 3
        rectangle = Rectangle(x1, y1, x2, y2)
        rectangle.drawToCanvas()

        exp = [['x', 'x', 'x', ' ', ' '], ['x', ' ', 'x', ' ', ' '], ['x', 'x', 'x', ' ', ' '], [' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_checkGeometryObjectConstraints(self):
        x11, y11, x21, y21 = 1, 1, 3, 3
        x12, y12, x22, y22 = 1, 1, 6, 3
        x13, y13, x23, y23 = -1, 1, 3, 3
        x14, y14, x24, y24 = 1, 1, 3, 5
        x15, y15, x25, y25 = 1, -1, 3, 3
        x16, y16, x26, y26 = 3, 3, 1, 1

        rectangel1 = Rectangle(x11, y11, x21, y21)
        rectangel2 = Rectangle(x12, y12, x22, y22)
        rectangel3 = Rectangle(x13, y13, x23, y23)
        rectangel4 = Rectangle(x14, y14, x24, y24)
        rectangel5 = Rectangle(x15, y15, x25, y25)
        rectangel6 = Rectangle(x16, y16, x26, y26)

        self.assertEqual(True, rectangel1.checkGeometryObjectConstraints())
        self.assertEqual(False, rectangel2.checkGeometryObjectConstraints())
        self.assertEqual(False, rectangel3.checkGeometryObjectConstraints())
        self.assertEqual(False, rectangel4.checkGeometryObjectConstraints())
        self.assertEqual(False, rectangel5.checkGeometryObjectConstraints())
        self.assertEqual(False, rectangel6.checkGeometryObjectConstraints())


if __name__ == '__main__':
    unittest.main()