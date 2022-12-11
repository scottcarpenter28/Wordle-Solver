from application.game_parts.scores import LetterScores
from typing import Union, List


def singulate_word(new_word: str) -> List[str]:
    return [c for c in new_word.lower()]


def test_guess(known_letters: list, includes_letters: list, excluded_letters: list, cur_word: str) -> bool:
    """

    :param known_letters:
    :param includes_letters:
    :param excluded_letters:
    :param cur_word:
    :return: True if word is valid, false if word is invalid
    """
    for index, char in enumerate(cur_word):
        # If the letter is excluded then skip it
        if char in excluded_letters[index]:
            return False

        # If the index has a known letter and cur letter does not match return
        elif not char == known_letters[index] and not known_letters[index] == " ":
            return False

        # If it is in the included letters continue
        elif char in includes_letters:
            continue

    # Check to see if all letters are matched
    for char in includes_letters:
        if char == " ":
            continue
        if char not in cur_word:
            return False

    return True


class CurrentGuess:
    def __init__(self, word_len: int = 5) -> None:
        self.cur_guess = [""] * word_len
        self.word_len = word_len

    def new_guess(self, word: str) -> None:
        if not len(word) == self.word_len:
            raise ValueError(f"Guessed word length of {len(word)} does not match {self.word_len}")
        self.cur_guess = [c for c in word.lower()]


class Word:
    def __init__(self, score: float = 0, word: str = "") -> None:
        self.score = score
        self.characters = singulate_word(word)
        self.word = word

    def __lt__(self, other) -> bool:
        return self.score < other.score

    def __le__(self, other) -> bool:
        return self.score <= other.score

    def __gt__(self, other) -> bool:
        return self.score > other.score

    def __ge__(self, other) -> bool:
        return self.score >= other.score

    def __eq__(self, other):
        return self.score == other.score


class Words:
    def __init__(
            self,
            character_scores: LetterScores,
            words_path: str = "./words.txt"
    ) -> None:
        with open(words_path, "r") as words_file:
            str_words = words_file.read()

        self.words = []
        for cur_word in str_words.split(","):
            self.words.append(Word(score=character_scores.get_word_score(cur_word), word=cur_word))

        self.words.sort(key=lambda next_word: next_word.score, reverse=True)
        print()

    def new_guess(
            self,
            known_letters: Union[str, list],
            includes_letters: Union[str, list],
            excluded_letters: list,
            return_count: int = 5
    ) -> list:
        if isinstance(known_letters, str):
            known_letters = singulate_word(known_letters)
        if isinstance(includes_letters, str):
            includes_letters = singulate_word(includes_letters)
        if isinstance(excluded_letters, str):
            excluded_letters = [singulate_word(group) for group in excluded_letters]

        matching_results = []
        for word in self.words:
            cur_word = word.word
            include_word = test_guess(
                known_letters,
                includes_letters,
                excluded_letters,
                cur_word
            )
            if include_word:
                matching_results.append(word.word)

        return matching_results[:return_count]
