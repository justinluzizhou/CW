import unittest
from src import wc


class testmethon(unittest.TestCase):

    def test1(self):
        actual = wc.count('testinputs/test1')
        expected = (7, 7, 14)
        self.assertEqual(expected, actual)

    def test2(self):
            actual = wc.count('testinputs/test2')
            expected = (10, 10, 47)
            self.assertEqual(expected, actual)

    def test3(self):
        actual = wc.count('testinputs/test0')
        expected = (0, 0, 0)
        self.assertEqual(expected, actual)

    def test4(self):
        actual = wc.count('testinputs/rainfall.py')
        expected = (25, 97, 711)
        self.assertEqual(expected, actual)

    def test5(self):
        actual = wc.count('testinputs/fizzbuzz.py')
        expected = (13, 71, 422)
        self.assertEqual(expected, actual)

    def test6(self):
        actual = wc.count('testinputs/test3')
        expected = (14, 14, 60)
        self.assertEqual(expected, actual)

    def test7(self):
        actual = wc.flagout([1, 0, 0], 14, 0, 0, 'testinputs/test1')
        expected ='14 testinputs/test'
        self.assertNotEqual(expected, actual)

    def test8(self):
        actual = wc.flagout([1, 1, 0], 25, 4, 90, 'testinputs/test1')
        expected = (25, 4, 'testinputs/test1')
        self.assertNotEqual(expected, actual)

    def test9(self):
        actual = wc.flagout([1, 1, 1], 2523, 434, 290, 'testinputs/rainfall')
        expected ='2523 434 290 testinputs/rainfall'
        self.assertNotEqual(expected, actual)

    def test10(self):
        actual = wc.out(['testinputs/test4'], [1, 1, 1])
        expected ='10 11 35 testinputs/test4'
        self.assertNotEqual(expected, actual)

    def test11(self):
        actual = wc.out(['testinputs/test4'], [1, 1, 0])
        expected ='10 11 testinputs/test4'
        self.assertNotEqual(expected, actual)

    def test12(self):
        actual = wc.out(['testinputs/test4', 'testinputs/test1'], [1, 1, 0])
        expected ='10 11 testinputs/test4\n 7 7 testinputs/test1\n 17 18 total'
        self.assertNotEqual(expected, actual)

    def test13(self):
        actual = wc.out(['testinputs/test4', 'testinputs/test1'], [1, 0, 0])
        expected ='10 testinputs/test4\n 7 testinputs/test1\n 17 total'
        self.assertNotEqual(expected, actual)

    def test14(self):
        actual = wc.out(['testinputs/test4', 'testinputs/test1', 'testinputs/test3'], [1, 1, 1])
        expected ='10 11 35 testinputs/test4\n 7 7 14 testinputs/test1\n 14 14 60 testinputs/test3\n 31 32 109 total'
        self.assertNotEqual(expected, actual)

    def test15(self):
        actual = wc.out(['testinputs/test4', 'testinputs/test1', 'testinputs/test3', 'testinputs/test4'], [1, 1, 1])
        expected ='    10 11 35 testinputs/test4\n 7 7 14 testinputs/test1\n 14 14 60 testinputs/test3\n 10 11 35 testinputs/test4\n 41 43 144 total\n'
        self.assertNotEqual(expected, actual)



if __name__ == "__main__":
    unittest.main()
