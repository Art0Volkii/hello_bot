import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    name = message.new_chat_members[0].username
    bot.send_message(message.chat.id, f"Ласкаво просимо, @{name}!")

@bot.message_handler(content_type=['text'])
def check(message):
    mm = message.chat_members.text
    bot.send_message(message.chat.id, mm)


bot.polling(none_stop=True)
