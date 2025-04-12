
import unittest
from entry_scorer import EntryScorer

class TestScorer(unittest.TestCase):
    def test_entry_scoring(self):
        entries = [{"rr": 2.0}]
        scorer = EntryScorer()
        scored = scorer.score_entries(entries)
        self.assertIn("confidence_score", scored[0])
        self.assertTrue(scored[0]["is_valid"])
