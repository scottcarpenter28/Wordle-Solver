import unittest
import sys
sys.path.insert(0, '../application')
from scores import LetterScores


class TestScoresClass(unittest.TestCase):
    def setUp(self) -> None:
        self.scores = LetterScores(score_csv_path="../letter_ranking.csv")

    def test_score_loading(self):
        self.assertTrue(isinstance(self.scores.scores_dict, dict))

    def test_uppercase_character_score(self):
        self.assertEqual(self.scores.get_letter_score("A"), 43.31)

    def test_lowercase_character_score(self):
        self.assertEqual(self.scores.get_letter_score("a"), 43.31)

    def test_missing_char_score(self):
        self.assertEqual(self.scores.get_letter_score("]"), 0)

    def test_full_word_sum(self):
        self.assertEqual(self.scores.get_word_score("ARISE"), 206.51)