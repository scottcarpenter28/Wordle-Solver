import unittest
import sys
sys.path.insert(0, "../application")
from words import Words, Word
from scores import LetterScores


class TestWordsClass(unittest.TestCase):
    def test_new_words_files(self):
        temp = Words(
            character_scores=LetterScores(score_csv_path="../letter_ranking.csv"),
            words_path='../words.txt'
        )
        self.assertTrue(isinstance(temp, Words))

    def test_less_than(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=102, word="camps")
        self.assertTrue(w1 < w2)

    def test_less_than_or_equal(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=100, word="camps")
        self.assertTrue(w1 <= w2)

    def test_greater_than(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=102, word="camps")
        self.assertTrue(w2 > w1)

    def test_greater_than_or_equal(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=100, word="camps")
        self.assertTrue(w2 >= w1)

    def test_equal_to(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=100, word="camps")
        self.assertTrue(w2 == w1)

    def test_not_equal_to(self):
        w1 = Word(score=100, word="Arise")
        w2 = Word(score=102, word="camps")
        self.assertTrue(w2 != w1)

    def test_guessing(self):
        temp = Words(
            character_scores=LetterScores(score_csv_path="../letter_ranking.csv"),
            words_path='../solutions.txt'
        )

        result = temp.new_guess(
            known_letters=" aive",
            includes_letters="ia",
            excluded_letters=[
                "wrti",
                "wrt",
                "wrta",
                "wrt",
                "wrt",
            ],
            return_count=5000
        )
        print(result)
        print(len(result))


if __name__ == '__main__':
    unittest.main()
