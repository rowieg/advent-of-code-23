import unittest
from days import eight

class TestPuzzleEight(unittest.TestCase):

    def test_convert_instructions(self):
        instructions = "RLLRLRLLLRLRLR"

        result = eight.convert_instructions(instructions)

        self.assertEqual(result, "10010100010101")

    def test_convert_map(self):
        map = [
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)",
        ]

        expected_map = {
            "AAA": ("BBB", "CCC"),
            "BBB": ("DDD", "EEE"),
            "CCC": ("ZZZ", "GGG"),
            "DDD": ("DDD", "DDD"),
            "EEE": ("EEE", "EEE"),
            "GGG": ("GGG", "GGG"),
            "ZZZ": ("ZZZ", "ZZZ"),
        }

        converted_map = eight.convert_map(map)
        self.assertEqual(converted_map, expected_map)

    def test_count_steps(self):
        instructions = "LLR"
        map = [
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        converted_instructions = eight.convert_instructions(instructions)
        converted_map = eight.convert_map(map)
        steps = eight.count_steps(converted_instructions, converted_map)
        self.assertEqual(steps, 6)

    def test_count_steps_as_ghost(self):
        instructions = "LR"
        map = [
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ]
        converted_instructions = eight.convert_instructions(instructions)
        converted_map = eight.convert_map(map)
        steps = eight.count_steps_as_ghost(converted_instructions, converted_map)
        self.assertEqual(steps, 6)



    # def test_puzzle_a_returns_number_from_string(self):
    #     input = [
    #       "two1nine",
    #       "eightwothree",
    #       "abcone2threexyz",
    #       "xtwone3four",
    #       "4nineeightseven2",
    #       "zoneight234",
    #       "7pqrstsixteen",
    #       "eighthree",
    #     ]
    #     result = one.puzzle_a(input)
    #     test_result = 281 + 83
    #     self.assertEqual(result, test_result)

if __name__ == '__main__':
    unittest.main()