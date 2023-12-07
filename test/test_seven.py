import unittest
from days import seven

class TestStringMethods(unittest.TestCase):

    def test_identify_hand(self):
        self.assertEqual(seven.identify_hand("AAAAA"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("AAAAK"), "four_of_a_kind")
        self.assertEqual(seven.identify_hand("AAAKK"), "full_house")
        self.assertEqual(seven.identify_hand("AAA23"), "three_of_a_kind")
        self.assertEqual(seven.identify_hand("AAQQ7"), "two_pair")
        self.assertEqual(seven.identify_hand("AA234"), "one_pair")
        self.assertEqual(seven.identify_hand("23456"), "high_card")
        self.assertEqual(seven.identify_hand("AAJQ7"), "three_of_a_kind")
        self.assertEqual(seven.identify_hand("AAQQ7"), "two_pair")
        self.assertEqual(seven.identify_hand("QJJJ3"), "four_of_a_kind")
        self.assertEqual(seven.identify_hand("QQJJ7"), "four_of_a_kind")
        self.assertEqual(seven.identify_hand("QQQJ7"), "four_of_a_kind")
        self.assertEqual(seven.identify_hand("AAAAJ"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("AAAJJ"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("AAJJJ"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("AJJJJ"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("JJJJJ"), "five_of_a_kind")
        self.assertEqual(seven.identify_hand("AAQQJ"), "full_house")
        self.assertEqual(seven.identify_hand("QQJ23"), "three_of_a_kind")
        self.assertEqual(seven.identify_hand("QJJ23"), "three_of_a_kind")
        self.assertEqual(seven.identify_hand("QJJK3"), "three_of_a_kind")
        self.assertEqual(seven.identify_hand("QQKK3"), "two_pair")



    def test_order_hands(self):
        list = [
            ("32T3K", 765),
            ("T55J5", 684),
            ("KK677", 28),
            ("KTJJT", 220),
            ("QQQJA", 483),
        ]
        expected_order = {
            "five_of_a_kind": [],
            "four_of_a_kind": [
                ("T55J5", 684),
                ("KTJJT", 220),
                ("QQQJA", 483),
            ],
            "full_house": [],
            "three_of_a_kind": [
            ],
            "two_pair": [
                ("KK677", 28),
            ],
            "one_pair": [
                ("32T3K", 765)
            ],
            "high_card": []
        }

        ordered_hand = seven.get_ordered_hand(list)
        self.assertEqual(ordered_hand, expected_order)
    
    def test_map_cards(self):
        my_tuple = ('KTJJT', 220)
        mapped_hand = seven.map_cards(my_tuple)
        self.assertEqual(mapped_hand, ("BEPPE", 220))

    def test_get_ranked_hand(self):
        list = [
            ('KTJJT', 220), 
            ("T55J5", 684),
            ("QQQJA", 483),
            ('KK677', 28),
            ("AAKJA", 987),
            ("AQKJA", 877),
            ("AJKQJ", 123),
        ]

        expected_list = [
            ("AAKJA", 987),
            ("AQKJA", 877),
            ("AJKQJ", 123),
            ('KK677', 28),
            ('KTJJT', 220), 
            ("QQQJA", 483),
            ("T55J5", 684),
        ]

        ranked_list = seven.get_rank_hands(list)
        self.assertEqual(ranked_list, expected_list)


    def test_order_hands_with_rank(self):

        hands = {
            "five_of_a_kind": [],
            "four_of_a_kind": [
                ("T55J5", 684),
                ("KTJJT", 220),
                ("QQQJA", 483),
            ],
            "full_house": [],
            "three_of_a_kind": [
            ],
            "two_pair": [
                ("KK677", 28),
            ],
            "one_pair": [
                ("32T3K", 765)
            ],
            "high_card": []
        }

        expected_ranked_game = {
            "five_of_a_kind": [],
            "four_of_a_kind": [
                ("KTJJT", 220),
                ("QQQJA", 483),
                ("T55J5", 684),
            ],
            "full_house": [],
            "three_of_a_kind": [
            ],
            "two_pair": [
                ("KK677", 28),
            ],
            "one_pair": [
                ("32T3K", 765)
            ],
            "high_card": []
        }

        ranked_game = seven.get_ranked_game(hands)
        self.assertEqual(ranked_game, expected_ranked_game)
    def test_count_hands(self):
        game = {
          "five_of_a_kind": [],
          "four_of_a_kind": [],
          "full_house": [],
          "three_of_a_kind": [
              ("QQQJA", 483),
              ("T55J5", 684),
          ],
          "two_pair": [
              ("KK677", 28),
              ("KTJJT", 220)
          ],
          "one_pair": [
              ("32T3K", 765)
          ],
          "high_card": []
        }
        hands = seven.count_hands(game)
        self.assertEqual(hands, 5)

    def test_calculate_winnings(self):
      game = {
        "five_of_a_kind": [],
            "four_of_a_kind": [
                ("KTJJT", 220),
                ("QQQJA", 483),
                ("T55J5", 684),
            ],
            "full_house": [],
            "three_of_a_kind": [
            ],
            "two_pair": [
                ("KK677", 28),
            ],
            "one_pair": [
                ("32T3K", 765)
            ],
            "high_card": []
      }
      winnings = seven.calculate_winnings(game)
      self.assertEqual(winnings, 5905)

if __name__ == '__main__':
    unittest.main()