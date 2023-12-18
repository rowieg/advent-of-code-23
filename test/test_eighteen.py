import unittest
from days import eighteen

class TestStringMethods(unittest.TestCase):

    def test_get_numbers_basic(self):
        
        points = [
            (0,0),
            (0,3),
            (3,3),
            (3,0),
        ]
        
        area = eighteen.calculate_area(points)
        
        self.assertEqual(area, 16)

    def test_extract_basic_points(self):
        
        data = [
            "R 2 (#70c710)",
            "D 2 (#0dc571)",
            "L 2 (#5713f0)",
            "U 2 (#d2c081)",
        ]
        
        points = eighteen.extract_points(data)
        area = eighteen.calculate_area(points)
        self.assertEqual(area, 9)

    def test_extract_points(self):
        
        data = [
            "R 6 (#70c710)",
            "D 5 (#0dc571)",
            "L 2 (#5713f0)",
            "D 2 (#d2c081)",
            "R 2 (#59c680)",
            "D 2 (#411b91)",
            "L 5 (#8ceee2)",
            "U 2 (#caa173)",
            "L 1 (#1b58a2)",
            "U 2 (#caa171)",
            "R 2 (#7807d2)",
            "U 3 (#a77fa3)",
            "L 2 (#015232)",
            "U 2 (#7a21e3)",
        ]
        
        points = eighteen.extract_points(data)
        area = eighteen.calculate_area(points)
        self.assertEqual(area, 62)

if __name__ == '__main__':
    unittest.main()