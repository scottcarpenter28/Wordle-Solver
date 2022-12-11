from typing import Tuple
from random import randint
from scores import LetterScores
from words import Words


class Game:
    def __init__(self, answer: str, allowed_guesses: int = 6, word_length: int = 6):
        self.answer = answer
        self.allowed_guesses = allowed_guesses
        self.current_guesses = 0
        self.word_length = word_length
        self.guesses = []
        self.excluded_letters = [""] * word_length

    def guess(self, word: str) -> Tuple[str, str, list]:
        self.current_guesses += 1
        self.guesses.append(word)

        known_letters = ""
        found_letters = ""
        for index, letter in enumerate(word):
            if letter == self.answer[index]:
                known_letters += letter
            else:
                self.excluded_letters[index] += letter
                known_letters += " "

            if letter in self.answer:
                found_letters += letter
            for c in range(len(word)):
                if letter not in self.answer and letter not in self.excluded_letters[c]:
                    self.excluded_letters[c] += letter

        return known_letters, found_letters, self.excluded_letters


if __name__ == "__main__":
    cur_game = Game(answer="naive", allowed_guesses=6, word_length=5)
    temp = Words(
        character_scores=LetterScores(score_csv_path="../../letter_ranking.csv"),
        words_path='../../solutions.txt'
    )

    guess = 1
    k, f, e = "     ", "     ", cur_game.excluded_letters
    result = temp.new_guess(
        known_letters=k,
        includes_letters=f,
        excluded_letters=e,
        return_count=50
    )
    random_guess = randint(0, len(result) - 1)
    print(f"Guess {guess}: {result[random_guess]}")

    while len(result) != 1:
        guess += 1
        k, f, e = cur_game.guess(result[random_guess])
        result = temp.new_guess(
            known_letters=k,
            includes_letters=f,
            excluded_letters=e,
            return_count=50
        )
        random_guess = randint(0, len(result) - 1)
        print(f"Guess {guess}: {result[random_guess]}")
        if result[random_guess] == cur_game.answer:
            print("You win!")
            break
    print()
