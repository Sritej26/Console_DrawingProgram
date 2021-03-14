import unittest
import sys
sys.path.append("C:/Users/Sritej. N/Downloads/ConsoleDraw")
from InputParameterValidation import parseInputArg, validateInputString, validateInputArgv


class TestInputParameterValidation(unittest.TestCase):

    def test_parseInputArg(self):
        self.assertEqual([], parseInputArg(["Q", "a"]))
        self.assertEqual(["Q", 1], parseInputArg(["Q", "1"]))
        self.assertEqual(["L", 1, 2, 4, 2], parseInputArg(["L", "1", "2", "4", "2"]))
        self.assertEqual(["R", 1, 2, 3, 4], parseInputArg(["R", "1", "2", "3", "4"]))
        self.assertEqual(["B", 1, 2, "o"], parseInputArg(["B", "1", "2", "o"]))

    def test_validateInputString(self):
        self.assertEqual(True, validateInputString("L 1 2 3 2"))

    def test_validateInputString_noInputStr(self):
        self.assertEqual(False, validateInputString(""))

    def test_validateInputString_doubleChar(self):
        self.assertEqual(False, validateInputString('T1 2 3 4'))

    def test_validateInputString_GeoTypeNoChar(self):
        self.assertEqual(False, validateInputString('1 2 3 4'))

    def test_validateInputArgv_correctNumberOfInputVariables(self):
        self.assertEqual(True, validateInputArgv(["Q"]))
        self.assertEqual(True, validateInputArgv(["C", 20, 5]))
        self.assertEqual(True, validateInputArgv(['L', 1, 2, 3, 2]))
        self.assertEqual(True, validateInputArgv(['R', 1, 2, 3, 4]))
        self.assertEqual(True, validateInputArgv(['B', 1, 2, 'o']))

    def test_validateInputArgv_wrongNumberOfInputVariables(self):
        self.assertEqual(False, validateInputArgv(['Q', 1]))
        self.assertEqual(False, validateInputArgv(['C', 20]))
        self.assertEqual(False, validateInputArgv(['L', 1, 2, 3]))
        self.assertEqual(False, validateInputArgv(['R', 1, 2, 3]))
        self.assertEqual(False, validateInputArgv(['B', 1]))


if __name__ == '__main__':
    unittest.main()
