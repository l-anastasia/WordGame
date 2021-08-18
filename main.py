from word_game import WordGame

from data_handler import prepare_all_words_list


def main():
    all_words = prepare_all_words_list("words.txt")
    game = WordGame(all_words)
    answer = 0
    while True:

        word = input("enter your word: ").lower()

        verdict = game.check_word(word)
        if verdict is WordGame.Verdict.NOT_WORD:
            return None
        elif verdict is WordGame.Verdict.USED_WORD:
            return None

        answer = game.next_word(word)

        if answer == 1:
            print("I won")
            break

        if answer == 2:
            print("You won")
            break

        if answer:
            print(answer)
            game.prev_word = answer


if __name__ == "__main__":
    main()
