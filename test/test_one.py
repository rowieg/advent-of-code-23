import unittest
from days import one

class TestStringMethods(unittest.TestCase):

    def test_puzzle_a_returns_number(self):
        input = [
          "1abc2",
          "pqr3stu8vwx",
          "a1b2c3d4e5f",
          "treb7uchet",
        ]
        result = one.puzzle_a(input)
        test_result = 142
        self.assertEqual(result, test_result)

    def test_puzzle_a_returns_number_from_string(self):
        input = [
          "two1nine",
          "eightwothree",
          "abcone2threexyz",
          "xtwone3four",
          "4nineeightseven2",
          "zoneight234",
          "7pqrstsixteen",
          "eighthree",
        ]
        result = one.puzzle_a(input)
        test_result = 281 + 83
        self.assertEqual(result, test_result)

if __name__ == '__main__':
    unittest.main()