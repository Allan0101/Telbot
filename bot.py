import telebot
bot = telebot.TeleBot('919261879:AAH7Vto0oADnmCr6ljE85T5e4WOxPscwqtM')

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)