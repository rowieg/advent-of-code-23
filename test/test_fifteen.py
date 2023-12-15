import unittest
from days import fifteen

class TestDayFourteen(unittest.TestCase):
    
    def test_puzzle_1(self):
      test_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")
      self.assertEqual(fifteen.puzzle_1(test_data), 1320)
      
    def test_initnumber_by_string(self):
      
      self.assertEqual(fifteen.initnumber_by_string("HASH"), 52)
      self.assertEqual(fifteen.initnumber_by_string("rn=1"), 30)
      self.assertEqual(fifteen.initnumber_by_string("cm-"), 253)
      self.assertEqual(fifteen.initnumber_by_string("qp=3"), 97)
      self.assertEqual(fifteen.initnumber_by_string("cm=2"), 47)
      
      

if __name__ == "__main__":
    unittest.main()
