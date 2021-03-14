import unittest
import sys
sys.path.append("C:/Users/Sritej. N/Downloads/ConsoleDraw")
from Canvas import Canvas
from GeometryType.Line import Line
from GeometryType.BucketFill import BucketFill


class TestBlock(unittest.TestCase):

    def setUp(self):
        self.w = 5
        self.h = 4
        self.canvas = Canvas(self.w, self.h)

    def test__drawToCanvas(self):
        line = Line(3, 1, 3, 4)
        line.drawToCanvas()
        b = BucketFill(1, 2, 'o')
        b.drawToCanvas()
        exp = [['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' '], ['o', 'o', 'x', ' ', ' ']]
        self.assertEqual(exp, self.canvas.canvasArray)

    def test_checkGeometryObjectConstraints(self):
        b1 = (1, 2)
        b2 = BucketFill(6, 2)
        b3 = BucketFill(1, 6)
        b4 = BucketFill(-1, 2)
        b5 = BucketFill(1, -1)

        self.assertEqual(True, b1.checkGeometryObjectConstraints())
        self.assertEqual(False, b2.checkGeometryObjectConstraints())
        self.assertEqual(False, b3.checkGeometryObjectConstraints())
        self.assertEqual(False, b4.checkGeometryObjectConstraints())
        self.assertEqual(False, b5.checkGeometryObjectConstraints())


if __name__ == '__main__':
    unittest.main()
