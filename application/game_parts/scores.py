import pandas as pd
from typing import List


class LetterScores:
    def __init__(self, score_csv_path: str = "./score.csv") -> None:
        """
        Creates the scoring object to look up the values of strings
        :param score_csv_path:
        """
        scores_df = pd.read_csv(score_csv_path)

        temp_scores = scores_df.to_dict()
        letters: List[str] = list(temp_scores.get("letter", {}).values())
        scores: List[float] = list(temp_scores.get("score", {}).values())
        percentages: List[float] = list(temp_scores.get("percentage", {}).values())

        self.scores_dict = {}
        for i, letter in enumerate(letters):
            self.scores_dict[letter.lower()] = {
                "score": scores[i],
                "percentage": percentages[i]
            }

    def get_letter_score(self, char: str = None) -> float:
        """
        Finds and returns the value of a character
        :param char: A character to get the score of
        :return: A value representing the character. 0 if no value was found
        """
        result = self.scores_dict.get(char.lower(), {})
        return result.get("score", 0)

    def get_word_score(self, word: str) -> float:
        """
        Determines the value of a words. Duplicate letters removed.
        :param word: The string to loop through
        :return: The sum of all char scores
        """
        clean_word = word.lower().strip()

        unique_characters = []
        score_count = 0
        for char in clean_word:
            if char in unique_characters:
                continue

            unique_characters.append(char)
            score_count += self.get_letter_score(char)

        return score_count
