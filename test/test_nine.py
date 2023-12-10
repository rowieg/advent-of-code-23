import unittest
import json

from days import nine

class TestDayNine(unittest.TestCase):

    def test_calculate_number(self):
        
        numbers = [0, 3, 6, 9, 12, 15]
        result = nine.puzzle_1(numbers)
        
        self.assertEqual(result, 18)

    def test_calculate_numbers_list(self):
        numbers_list = [
            [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45],
        ]
        results = [
            18,
            28,
            68
        ]
        for index, numbers in enumerate(numbers_list):
            number = nine.puzzle_1(numbers)
            self.assertEqual(number, results[index])


if __name__ == '__main__':
    unittest.main()