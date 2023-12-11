import unittest

from days import ten

class TestDayTen(unittest.TestCase):

    def test_directions(self):
        self.assertEqual(True, ten.from_top((1,1), (1,2)))
        self.assertEqual(True, ten.from_right((1,1), (0,1)))
        self.assertEqual(True, ten.from_bottom((1,1), (1,0)))
        self.assertEqual(True, ten.from_left((1,1), (2,1)))

    def test_J(self):
        
        numbers = [
            "...",
            ".S7",
            ".LJ",
        ]
        result = ten.puzzle_1(numbers)
        expected = [False, (True, 4), (True, 4), False]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()