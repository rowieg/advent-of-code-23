import unittest
from days import three

class TestStringMethods(unittest.TestCase):

    def test_get_numbers(self):
        
        data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        numbers = three.get_numbers(data)
        self.assertEqual(numbers, 4361)

    def test_get_gear(self):
        
        data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598..",
        ]
        gears = three.get_gears(data)
        self.assertEqual(gears, [(3, 1), (3, 4), (5, 8)])

    def no_test_get_gear_ratio(self):
        
        data = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.*",
        ]
        gears = [(3, 1), (3, 4), (5, 8), (9, 9)]
        gear_ratios = three.get_gear_ratio(data, gears)
        self.assertEqual(gear_ratios, [16345, 451490])

        gear_ratio_sum = 0
        for gear_ratio in gear_ratios:
            gear_ratio_sum = gear_ratio_sum + gear_ratio
        self.assertEqual(gear_ratio_sum, 467835)


if __name__ == '__main__':
    unittest.main()