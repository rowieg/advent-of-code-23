import unittest
import json

from days import five

class TestStringMethods(unittest.TestCase):

    def test_converter(self):
        
        seeds = [79 , 14, 55, 13]
        locations = []
        lowest_location = 0

        for seed in seeds:
            result = 0
            print_seed = seed
            #print("seed-to-soil map:")
            soil_tuples = [
                (50, 98, 2),
                (52, 50, 48)
            ]
            result = five.convert_tuples(soil_tuples, seed)
            print_soil = result

            #print("soil-to-fertilizer map:")
            fertilizer_tuples = [
                (0, 15, 37),
                (37, 52, 2),
                (39, 0, 15),
            ]
            result = five.convert_tuples(fertilizer_tuples, result)
            print_fert = result

            #print("fertilizer-to-water map:")
            water_tuples = [
                (49, 53, 8),
                (0, 11, 42),
                (42, 0, 7),
                (57, 7, 4),
            ]

            result = five.convert_tuples(water_tuples, result)
            print_water = result

            #print("water-to-light map:")
            light_tuples = [
                (88, 18, 7),
                (18, 25, 70),
            ]

            result = five.convert_tuples(light_tuples, result)
            print_light = result

            #print("light-to-temperature map:")
            temp_tuples = [
                (45, 77, 23),
                (81, 45, 19),
                (68, 64, 13),
            ]

            result = five.convert_tuples(temp_tuples, result)
            print_temp = result

            #print("temperature-to-humidity map:")
            humi_tuples = [
                (0, 69, 1),
                (1, 0, 69),
            ]

            result = five.convert_tuples(humi_tuples, result)
            print_humi = result

            #print("humidity-to-location map:")
            local_tuples = [
                (60, 56, 37),
                (56, 93, 4),
            ]
            result = five.convert_tuples(local_tuples, result)
            print_loc = result

            locations.append(result)            

        for location in locations:
            if lowest_location == 0:
                lowest_location = location

            if location < lowest_location:
                lowest_location = location
        
        self.assertEqual(lowest_location, 35)

if __name__ == '__main__':
    unittest.main()