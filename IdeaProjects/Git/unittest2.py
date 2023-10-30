import program
import unittest

class TestAvg(unittest.TestCase):
    def test_neg(self):
        self.assertEqual(program.avg([2,-4,6,8]),3)

if __name__ == '__main__':
    unittest.main()