from word_game import WordGame

from data_handler import prepare_all_words_list

import telebot
with open("C:\\files\\idtoken.txt", "r") as id:
    token = id.read()


bot = telebot.TeleBot(token)

game_dict = {}

m_sur = 'thank you for the game, if you want to play again type /newgame'
m_start = (
    'This game is simple.'
    'You say a word, then bot will give you a word,'
    'that starts with the last letter of the previous word and so on.'
    'Type /newgame to start')
m_no_game = 'you need to start a new game first, type /newgame'
m_end = 'thank you for the game, if you want to play again type /newgame'
m_not_a_word = 'This is not a word'
m_used_word = 'This word has been used already'
m_incorrect_word = 'Your word is not correct, try again'


@bot.message_handler(commands=['start'])
def start(message):
    # 1
    bot.send_message(message.from_user.id, m_start)



@bot.message_handler(commands=['newgame'])
def new_game(message):
    user_id = message.from_user.id
    all_words = prepare_all_words_list("words.txt")
    game_dict[user_id] = WordGame(all_words)
    game = WordGame(all_words)
    # 2
    bot.send_message(user_id, 'enter your word, please')


@bot.message_handler(commands=['surrender'])
def surrender(message):
    user_id = message.from_user.id
    del game_dict[user_id] # 3
    bot.send_message(user_id, m_sur)


@bot.message_handler(content_types=['text'])
def play_game(message):
    user_id = message.from_user.id
    # 4.1
    if user_id not in game_dict:
        bot.send_message(user_id, m_no_game)
        return

    word = message.text.lower()

    verdict = game_dict[user_id].check_word(word)
    if verdict is WordGame.Verdict.NOT_A_WORD:
        bot.send_message(user_id, m_not_a_word)
        return

    elif verdict is WordGame.Verdict.USED_WORD:
        bot.send_message(user_id, m_used_word)
        return

    elif verdict is WordGame.Verdict.INCORRECT_WORD:
        bot.send_message(user_id, m_incorrect_word)
        return

    answer = game_dict[user_id].next_word(word)
    # 4.2
    if not answer:
        bot.send_message(user_id, 'You won')
        del game_dict[user_id] # 4.3 = 3
        bot.send_message(user_id, m_end)

    bot.send_message(user_id, answer)
    game_dict[user_id].prev_word = answer


# if __name__ == "__main__":
#     main()


bot.polling(none_stop=True, interval=0)
