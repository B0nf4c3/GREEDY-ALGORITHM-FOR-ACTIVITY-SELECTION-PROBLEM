import unittest
from greedy_activity_selection import greedy_activity_selection
from dp_activity_selection import dp_activity_selection

class TestActivitySelection(unittest.TestCase):
    def setUp(self):
        self.activities = [(1, 3), (2, 5), (4, 7), (1, 8), (5, 9), (8, 10)]
    
    def test_greedy(self):
        result = greedy_activity_selection(self.activities)
        expected = [(1, 3), (4, 7), (8, 10)]
        self.assertEqual(result, expected)
    
    def test_dp(self):
        result = dp_activity_selection(self.activities)
        expected = 3
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
