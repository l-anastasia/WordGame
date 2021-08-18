from word_game import WordGame

from data_handler import prepare_all_words_list

import telebot
with open("C:\\files\\idtoken.txt", "r") as id:
    token = id.read()


bot = telebot.TeleBot(token)

@bot.message_handler(content_types=['text'])
def message_handler(message):
    all_words = prepare_all_words_list("words.txt")
    game = WordGame(all_words)
    answer = 0
    # to create /start handler
    # to create a dict {user_id: game}
    # to create /new_game - create a new game for user_id
    # to create /surrender - finish the game



    # bot.send_message(message.from_user.id, 'enter your word, please')
    word = message.text.lower()

    verdict = game.check_word(word)
    if verdict is WordGame.Verdict.NOT_WORD:
        bot.send_message(message.from_user.id, 'This is not a word')
        return

    elif verdict is WordGame.Verdict.USED_WORD:
        bot.send_message(message.from_user.id, 'This word has been used already')
        return

    elif verdict is WordGame.Verdict.INCORRECT_WORD:
        bot.send_message(message.from_user.id, 'Your word is not correct, try again')
        return

    answer = game.next_word(word)

    if answer == 1:
        bot.send_message(message.from_user.id, 'I won')
        return

    if answer == 2:
        bot.send_message(message.from_user.id, 'You won')
        return

    if answer:
        bot.send_message(message.from_user.id, answer)
        game.prev_word = answer


# if __name__ == "__main__":
#     main(message)


bot.polling(none_stop=True, interval=0)
