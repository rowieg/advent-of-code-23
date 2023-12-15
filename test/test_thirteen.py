import unittest

from days import thirteen

test_data = [
    "#.##..##.",
    "..#.##.#.",
    "##......#",
    "##......#",
    "..#.##.#.",
    "..##..##.",
    "#.#.##.#.",
    "",
    "#...##..#",
    "#....#..#",
    "..##..###",
    "#####.##.",
    "#####.##.",
    "..##..###",
    "#....#..#",
]

test_data_two = [
    "#..#...#.#..#",
    "#..#####.####",
    "#..######....",
    ".##...####.#.",
    ".##.##.#.####",
    "#..#.###.##.#",
    ".....###.#.#.",
    ".##..##..##..",
    "....#.#####..",
    "....###..##.#",
    "....####.##.#",
    
    # "..#.#......#.",
    # "###.#.####.#.",
    # "##.##.#..#.##",
    # "##..#.####.#.",
    # "...###.##.###",
    # "###.##.##.##.",
    # "###..##..#...",
    # "###..##..##..",
    # "####.#.##.#.#",

    # "..#.#......#.",
    # "###.#.####.#.",
    # "##.##.#..#.##",
    # "##..#.####.#.",
    # "...###.##.###",
    # "###.##.##.##.",
    # "###..##..#...",
    # "###..##..##..",
    # "####.#.##.#.#",
]

class TestDayThirteen(unittest.TestCase):

    def test_directions(self):
        
        matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
        ]

        expected = [
            [1,4,7],
            [2,5,8],
            [3,6,9]
        ]

        fliped_matrix = thirteen.flip_matrix(matrix)

        self.assertEqual(expected, fliped_matrix)

    def test_extract_game_maps(self):
        game_maps = thirteen.extract_game_maps(test_data)

        self.assertEqual(len(game_maps), 2)

        game_map = [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ]

        self.assertEqual(game_maps[0], game_map)

    def test_convert_game_map(self):
        game_map = [
            "#.##..##.",
            "..#.##.#.",
            "##......#",
            "##......#",
            "..#.##.#.",
            "..##..##.",
            "#.#.##.#.",
        ]

        expected = [
            [1,0,1,1,0,0,1,1,0],
            [0,0,1,0,1,1,0,1,0],
            [1,1,0,0,0,0,0,0,1],
            [1,1,0,0,0,0,0,0,1],
            [0,0,1,0,1,1,0,1,0],
            [0,0,1,1,0,0,1,1,0],
            [1,0,1,0,1,1,0,1,0],
        ]

        converted_map = thirteen.convert_game_map(game_map)

        self.assertEqual(converted_map, expected)

    def test_find_mirror_line_index(self):
        converted_map = [
            [1,0,1,1,0,0,1,1,0],
            [0,0,1,0,1,1,0,1,0],
            [1,1,0,0,0,0,0,0,1],
            [1,1,0,0,0,0,0,0,1],
            [0,0,1,0,1,1,0,1,0],
            [0,0,1,1,0,0,1,1,0],
            [1,0,1,0,1,1,0,1,0],
        ]

        index_x = thirteen.find_mirror_line_index(converted_map)
        index_y = thirteen.find_mirror_line_index(thirteen.flip_matrix(converted_map))
        self.assertEqual(index_x, 2)
        self.assertEqual(index_y, 4)

    def test_find_perfect_mirror(self):
        game_maps = thirteen.extract_game_maps(test_data)
        results = []
        converted_game_maps = []

        for map in game_maps:
            converted_game_map = thirteen.convert_game_map(map)
            converted_game_maps.append(converted_game_map)

        for game_map in converted_game_maps:
            
          index_x = thirteen.find_mirror_line_index(game_map)
          index_y = thirteen.find_mirror_line_index(thirteen.flip_matrix(game_map))
          results.append(thirteen.find_perfect_mirror(game_map, index_x, index_y))

        self.assertEqual(results[0], ("Vertical", 5))
        self.assertEqual(results[1], ("Horizontal", 4))

    def test_puzzle_1(self):
        result = thirteen.puzzle_1(test_data_two)
        self.assertEqual(result, 405)

if __name__ == '__main__':
    unittest.main()