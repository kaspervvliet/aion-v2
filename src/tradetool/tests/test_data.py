
import unittest
from tradetool.data import get_latest_data

class TestData(unittest.TestCase):
    def test_data_structure(self):
        data = get_latest_data("SOL/USD")
        self.assertIsInstance(data, list)
        self.assertTrue(all("timestamp" in d for d in data))
