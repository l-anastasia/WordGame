import unittest
from unittest import main
from enum import Enum

import os
wordgame_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(wordgame_dir_path)

from word_game import WordGame


class TestWordGame(unittest.TestCase):
    def setUp(self):
        self.words = ["cat", "tea", "apple", "egg"]
        self.word_game = WordGame(self.words)

    def test_check_word_OK(self):
        value = self.word_game.Verdict.OK
        check_result = self.word_game.check_word("cat")
        self.assertEqual(value, check_result)

    def test_check_word_NOT_A_WORD(self):
        value = self.word_game.Verdict.NOT_A_WORD
        check_result = self.word_game.check_word("aaa")
        self.assertEqual(value, check_result)

    def test_check_word_USED_WORD(self):
        self.word_game.used_words = ["tea"]
        value = self.word_game.Verdict.USED_WORD
        check_result = self.word_game.check_word("tea")
        self.assertEqual(value, check_result)

    def test_check_word_INCORRECT_WORD(self):
        self.word_game.prev_word = ["thunder"]
        value = self.word_game.Verdict.INCORRECT_WORD
        check_result = self.word_game.check_word("apple")
        self.assertEqual(value, check_result)

    def test_next_word_simple_positive(self):
        check_result = self.word_game.next_word("apple")
        self.assertTrue(check_result)

    def test_next_word_simple_negative(self):
        check_result = self.word_game.next_word("egg")
        self.assertFalse(check_result)

if __name__ == "__main__":
    unittest.main(verbosity=2)
