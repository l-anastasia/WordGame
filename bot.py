from word_game import WordGame

from data_handler import prepare_all_words_list

import telebot
with open("C:\\files\\idtoken.txt", "r") as id:
    token = id.read()


bot = telebot.TeleBot(token)

game_dict = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, 'here will be instraction some day')


@bot.message_handler(commands=['newgame'])
def new_game(message):
    user_id = message.from_user.id
    all_words = prepare_all_words_list("words.txt")
    game_dict[user_id] = WordGame(all_words)
    bot.send_message(message.from_user.id, user_id)
    bot.send_message(message.from_user.id, game_dict)
    bot.send_message(message.from_user.id, 'enter your word, please')


@bot.message_handler(commands=['surrender'])
def surrender(message):
    # user_id = message.from_user.id
    bot.send_message(message.from_user.id, game_dict)
    del game_dict[message.from_user.id]
    bot.send_message(message.from_user.id, 'thank you for the game, if you want to play again type /newgame')


@bot.message_handler(content_types=['text'])
def play_game(message):

    answer = 0
    # to create /start handler
    # to create a dict {user_id: game}
    # to create /new_game - create a new game for user_id
    # to create /surrender - finish the game
    word = message.text.lower()
    # user_id = message.from_user.id
    bot.send_message(message.from_user.id, message.from_user.id)
    verdict = game_dict[message.from_user.id].check_word(word)
    if verdict is WordGame.Verdict.NOT_WORD:
        bot.send_message(message.from_user.id, 'This is not a word')
        return

    elif verdict is WordGame.Verdict.USED_WORD:
        bot.send_message(message.from_user.id, 'This word has been used already')
        return

    elif verdict is WordGame.Verdict.INCORRECT_WORD:
        bot.send_message(message.from_user.id, 'Your word is not correct, try again')
        return

    answer = game_dict[message.from_user.id].next_word(word)

    if answer == 2:
        bot.send_message(message.from_user.id, 'You won')
        del game_dict[message.from_user.id]
        bot.send_message(message.from_user.id, 'thank you for the game, if you want to play again type /newgame')

    if answer != 2:
        bot.send_message(message.from_user.id, answer)
        game_dict[message.from_user.id].prev_word = answer


# if __name__ == "__main__":
#     main()


bot.polling(none_stop=True, interval=0)
