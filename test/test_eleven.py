import unittest
from math import comb
from days import eleven

class TestPuzzleEleven(unittest.TestCase):

    def test_expand_game_map(self):
        map = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#.....",
        ]

        coordinates = eleven.extract_universes_coordinates(map)
        print(eleven.caluclate_distances(coordinates))

        expected_map = [
            "....#........",
            ".........#...",
            "#............",
            ".............",
            ".............",
            "........#....",
            ".#...........",
            "............#",
            ".............",
            ".............",
            ".........#...",
            "#....#.......",
        ]

        extended_map = eleven.extend_game_map(map)

        self.assertEqual(extended_map, expected_map)

    
    def test_extract_universes_coordinates(self):
        map = [
            "....#........",
            ".........#...",
            "#............",
            ".............",
            ".............",
            "........#....",
            ".#...........",
            "............#",
            ".............",
            ".............",
            ".........#...",
            "#....#.......",
        ]

        coordinates = eleven.extract_universes_coordinates(map)

        expected_coordinates = [
            (0,2),
            (0,11),
            (1,6),
            (4,0),
            (5,11),
            (8,5),
            (9,1),
            (9,10),
            (12,7),
        ]

        self.assertEqual(coordinates,expected_coordinates)

    def test_calculate_distance(self):
        point_a = (0,2)
        point_b = (0,11)

        self.assertEqual(eleven.caluclate_distance(point_a, point_b), 9)

    def test_calculate_distances(self):
        expected_coordinates = [
            (0,2),
            (0,11),
            (1,6),
            (4,0),
            (5,11),
            (8,5),
            (9,1),
            (9,10),
            (12,7),
        ]

        self.assertEqual(eleven.caluclate_distances(expected_coordinates), 374)

if __name__ == '__main__':
    unittest.main()