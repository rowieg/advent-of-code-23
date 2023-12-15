import unittest
from days import fourteen

class TestDayFourteen(unittest.TestCase):
    test_data = [
      "O....#....",
      "O.OO#....#",
      ".....##...",
      "OO.#O....O",
      ".O.....O#.",
      "O.#..O.#.#",
      "..O..#O..O",
      ".......O..",
      "#....###..",
      "#OO..#....",
    ]
  
    row = "OO..O..#..O.O#..OO"
    
    def test_puzzle_1(self):
      result = fourteen.puzzle_1(self.test_data)
      self.assertEqual(result, 136)
    
    
    def test_convert_to_rows(self):
      rows = fourteen.convert_to_rows(self.test_data)
      expected_rows = [
        "OO.O.O..##",
        "...OO....O",
        ".O...#O..O",
        ".O.#......",
        ".#.O......",
        "#.#..O#.##",
        "..#...O.#.",
        "....O#.O#.",
        "....#.....",
        ".#.O.#O...",
      ]
    
      self.assertEqual(rows, expected_rows)
    
    def test_stone_index(self):
        
        stone_index = fourteen.get_stone_positions(self.row)
        stone_index_expected = [8,14]
        
        self.assertEqual(stone_index, stone_index_expected)
        
    def test_rolling_stones(self):
    
        row_parts = self.row.split("#")
        
        rolling_stones = fourteen.get_rolling_stones(row_parts)
        rolling_stones_expected = [3,2,2]
        
        self.assertEqual(rolling_stones, rolling_stones_expected)
        
    def test_calculate_sum(self):
      
      stone_index_expected = [8,14]
      rolling_stones_expected = [3,2,2]
      table_length = 18
      stone_sum = fourteen.calculate_stone_sum(stone_index_expected, rolling_stones_expected, table_length)
      stone_sum_expected = 18+17+16+10+9+4+3
      
      self.assertEqual(stone_sum, stone_sum_expected)

if __name__ == "__main__":
    unittest.main()
