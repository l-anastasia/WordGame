import unittest
from unittest import main

import os
wordgame_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

import sys
sys.path.append(wordgame_dir_path)

from word_game import WordGame


class TestWordGame(unittest.TestCase):
    def setUp(self):
        self.words = ["cat", "tea", "apple"]
        self.word_game = WordGame(self.words)

    def test_check_word_simple_positive(self):
        check_result = self.word_game.check_word("cat")
        self.assertTrue(check_result)

    def test_check_word_incorrect_word(self):
        check_result = self.word_game.check_word("aaa")
        self.assertFalse(check_result)

    def test_next_word_simple_positive(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity=2)