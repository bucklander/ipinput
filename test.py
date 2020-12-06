import unittest
from ipinput import routeLookup, openRouteTableFile, Route

class Unit_Testing(unittest.TestCase):
    def testECMP(self):
        result = routeLookup("1.1.1.1")
        self.assertEqual(len(result), 3)

    def testObj(self):
        result = routeLookup("1.1.1.1")
        self.assertFalse(isinstance(result[0], Route))

if __name__ == '__main__':
    unittest.main()