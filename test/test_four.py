import unittest
from days import four

class TestStringMethods(unittest.TestCase):

    def test_puzzle_a_returns_number(self):
        line = ([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53])

        matches = four.count_matches(line)
        self.assertEqual(matches, 4)

if __name__ == '__main__':
    unittest.main()