import unittest
from days import three

class TestStringMethods(unittest.TestCase):

    def test_game_map_function(self):
        
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

        
        # loop over all numbers 
        # check for symbol for each number
        # if symbol add number to list
        # sum up list


        sum = 4361

        self.assertEqual(3, 3)

    
if __name__ == '__main__':
    unittest.main()