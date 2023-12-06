import unittest
from days import six

class TestStringMethods(unittest.TestCase):

    def test_calculate_winner(self):
        
        race_set_one = six.claculate_race_set(7)
        winning_rounds = six.calculate_winning_rounds(race_set_one, 9)
        result_one = six.number_of_wins(winning_rounds)

        race_set_two = six.claculate_race_set(15)
        winning_rounds = six.calculate_winning_rounds(race_set_two, 40)
        result_two = six.number_of_wins(winning_rounds)

        race_set_three = six.claculate_race_set(30)
        winning_rounds = six.calculate_winning_rounds(race_set_three, 200)
        result_three = six.number_of_wins(winning_rounds)

        multiply_winning_rounds = result_one * result_two * result_three

        self.assertEqual(4, result_one)
        self.assertEqual(8, result_two)
        self.assertEqual(9, result_three)
        self.assertEqual(288, multiply_winning_rounds)

    
if __name__ == '__main__':
    unittest.main()