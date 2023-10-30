import program
import unittest

class TestAvg(unittest.TestCase):
    def test_pos(self):
        self.assertEqual(program.avg([2,4,6,8]),5)

if __name__ == '__main__':
    unittest.main()