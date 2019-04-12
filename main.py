import telebot
#import constants

token = "803170993:AAGKEDEBVLWUjRayvIFe7yJZl62FXKoks58"
bot = telebot.TeleBot(token)
#bot.send_message(421040739, "Privet")

#upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]
#message_from_user = last_upd.message

#print(message_from_user)

"""
@bot.message_handler(commands=['start'])
def handle_text(message):
    bot.send_message(message.chat.id, "Привет {0}, добро пожаловать в A Class Online! Напиши мне интересующи тебя вопрос и я тебе обязательно отвечу)".format(message.chat.first_name))
"""

upd = bot.get_updates()
last_upd = upd[0]
last_message_from_user = last_upd.message.text
print(last_message_from_user)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row('отправить ДЗ','задать вопрос')
    user_markup.row('Последнее ДЗ','Войти в online course')
    bot.send_message(message.chat.id, "Привет {0}, добро пожаловать в A Class Online! "
                                      "Напиши мне интересующи тебя вопрос и я тебе обязательно отвечу)".format(message.chat.first_name),
                     reply_markup=user_markup)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == "отправить ДЗ":
        bot.send_message(message.chat.id, "Отправь мне свое домашнее задание и мы его обязательно проверим!)\n"
                                          "Желательно все одним сообщением")
    elif last_message_from_user == "отправить ДЗ":
        bot.send_message(message.chat.id, "Круто! Как проверим я дам тебе знать)")
    elif message.text == "задать вопрос":
        bot.send_message(message.chat.id, "Какой вопрос тебя интересует?")
    elif message.text == "Последнее ДЗ":
        bot.send_message(message.chat.id, "Какой вопрос тебя интересует?")
        #document = open('‎/Users/ww/Downloads/Additional\ grammar\ language\ practice\ Grammar\ 37\ page_103.pdf ', 'rb')
        #bot.send_chat_action(message.from_user.id, 'upload_document')
        #bot.send_document(message.chat_id, document)
    else:
        bot.send_message(message.chat.id, "Сейчас заменю масло и приду)")


@bot.message_handler(content_types=['voice'])
def handle_audio(message):
    print(message)
    bot.send_message(message.chat.id, "Звучит не плохо {0}, но лучше отправлю преподователю)".format(message.chat.first_name))

bot.polling()