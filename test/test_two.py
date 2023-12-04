import unittest
from days import two

class TestStringMethods(unittest.TestCase):

    def test_game_class(self):
        
        g1 = two.Game(12, 13, 14)

        self.assertEqual(12, g1.boundary["red"])
        self.assertEqual(13, g1.boundary["green"])
        self.assertEqual(14, g1.boundary["blue"])

    def test_game_load_function(self):
        
        data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        
        g1 = two.Game(12, 13, 14)

        g1.import_game_data(data)
        game_data = g1.load_game_data()
        example_game_data = {
            1: {
                1: {"red": 4, "green": 0, "blue": 3},
                2: {"red": 1, "green": 2, "blue": 6},
                3: {"red": 0, "green": 2, "blue": 0}
            },
            2: {
                1: {"red": 0, "green": 2, "blue": 1},
                2: {"red": 1, "green": 3, "blue": 4},
                3: {"red": 0, "green": 1, "blue": 1}
            },
            3: {
                1: {"red": 20, "green": 8, "blue": 6},
                2: {"red": 4, "green": 13, "blue": 5},
                3: {"red": 1, "green": 5, "blue": 0}
            },
            4: {
                1: {"red": 3, "green": 1, "blue": 6},
                2: {"red": 6, "green": 3, "blue": 0},
                3: {"red": 14, "green": 3, "blue": 15}
            },
            5: {
                1: {"red": 6, "green": 3, "blue": 1},
                2: {"red": 1, "green": 2, "blue": 2}
            }
        }
        self.assertEqual(game_data[1], example_game_data[1])
        self.assertEqual(game_data[2], example_game_data[2])
        self.assertEqual(game_data[3], example_game_data[3])
        self.assertEqual(game_data[4], example_game_data[4])
        self.assertEqual(game_data[5], example_game_data[5])

    def test_get_possible_games(self):
        data = [
            "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
            "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
            "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
            "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
            "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        ]
        
        test_posible_games = [1, 2, 5]

        g1 = two.Game(12, 13, 14)

        g1.import_game_data(data)

        posible_games = g1.get_possible_games()
        self.assertEqual(posible_games, test_posible_games)

        game_sum = 0

        for game in posible_games:
            game_sum = game_sum + game
          
        self.assertEqual(game_sum, 8)


    
if __name__ == '__main__':
    unittest.main()