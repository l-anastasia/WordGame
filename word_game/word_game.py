from enum import Enum


class WordGame:
    def __init__(self, all_words):
        self.set_of_all_words = set(all_words)
        self.set_of_all_words.add("i give up")
        self.dict_of_all_words = {}

        self.used_words = []
        self.prev_word = None

        for word in self.set_of_all_words:
            if word[0] not in self.dict_of_all_words:
                self.dict_of_all_words[word[0]] = [word]
                continue
            self.dict_of_all_words[word[0]].append(word)

    class Verdict(Enum):
        OK = 0
        NOT_WORD = 1
        USED_WORD = 2
        INCORRECT_WORD = 3

    def check_word(self, word) -> Verdict:
        if word not in self.set_of_all_words:
            # print("This is not a word")
            return self.Verdict.NOT_WORD

        if word in self.used_words:
            # print("This word has been used already")
            return self.Verdict.USED_WORD

        # if word == ["i give up"]:
        #     return True

        if self.prev_word and word[0] != self.prev_word[-1]:
            # print("Your word is not correct, try again")
            return self.Verdict.INCORRECT_WORD

        return self.Verdict.OK

    def next_word(self, word):
        if word == "i give up":
            return 1

        self.used_words.append(word)
        self.dict_of_all_words[word[0]].remove(word)

        if not self.dict_of_all_words[word[-1]]: #checking if we have an answer
            return 2

        result = self.dict_of_all_words[word[-1]].pop()
        self.used_words.append(result)

        return result





