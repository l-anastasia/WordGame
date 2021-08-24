from word_game import WordGame

from data_handler import prepare_all_words_list

import telebot
with open("C:\\files\\idtoken.txt", "r") as id:
    token = id.read()


bot = telebot.TeleBot(token)

game_dict = {}

m_sur = 'thank you for the game, if you want to play again type /newgame'
m_start = 'here will be instractions some day'
m_no_game = 'you need to start a new game first, type /newgame'
m_end = 'thank you for the game, if you want to play again type /newgame'
m_not_a_word = 'This is not a word'
m_used_word = 'This word has been used already'
m_incorrect_word = 'Your word is not correct, try again'


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, m_start)


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
    bot.send_message(message.from_user.id, m_sur)


@bot.message_handler(content_types=['text'])
def play_game(message):

    if not game_dict:
        bot.send_message(message.from_user.id, m_no_game)
        return

    word = message.text.lower()

    verdict = game_dict[message.from_user.id].check_word(word)
    if verdict is WordGame.Verdict.NOT_A_WORD:
        bot.send_message(message.from_user.id, m_not_a_word)
        return

    elif verdict is WordGame.Verdict.USED_WORD:
        bot.send_message(message.from_user.id, m_used_word)
        return

    elif verdict is WordGame.Verdict.INCORRECT_WORD:
        bot.send_message(message.from_user.id, m_incorrect_word)
        return

    answer = game_dict[message.from_user.id].next_word(word)

    if not answer:
        bot.send_message(message.from_user.id, 'You won')
        del game_dict[message.from_user.id]
        bot.send_message(message.from_user.id, m_end)

    bot.send_message(message.from_user.id, answer)
    game_dict[message.from_user.id].prev_word = answer


# if __name__ == "__main__":
#     main()


bot.polling(none_stop=True, interval=0)
