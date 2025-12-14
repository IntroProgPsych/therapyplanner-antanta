#import all needed modules here
import unittest

#write all your tests below this line


#write your test suite here, in the main() function
def main():
    #call all your tets here, one on each line
    print("Starting tests suite...")
    
#please do not change the lines below
if __name__ == "__main__":
    main()

# starting point

import unittest
from app import interpret_load


class TestInterpretLoad(unittest.TestCase):

    def test_low_load(self):
        self.assertEqual(interpret_load(0), "Low")
        self.assertEqual(interpret_load(4), "Low")

    def test_moderate_load(self):
        self.assertEqual(interpret_load(5), "Moderate")
        self.assertEqual(interpret_load(9), "Moderate")

    def test_high_load(self):
        self.assertEqual(interpret_load(10), "High")
        self.assertEqual(interpret_load(15), "High")


if __name__ == "__main__":
    unittest.main()