import telebot
bot = telebot.TeleBot('919261879:AAH7Vto0oADnmCr6ljE85T5e4WOxPscwqtM')

@bot.message_handler(commands=['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1=types.KeyboardButton("Пункт 1")
	item2=types.keyboardButton("Пункт 2")
	
	markup.add(item1, item2)
	
	bot.send_message(message.chat.id, "Добро пожаловать,{0.first_name}!\"
		parse_mode='html', reply_markup=markup)
			 
@bot.message_handler(content_types=['text'])
def send(message):
	if message.chat.type=='private':
		if message.text == 'Пункт 1':
			 bot.send_message(message.chat.id, "Рез 1"
		elif message.text == 'Пункт 2':
			 bot.send_message(message.chat.id, "Рез 2"
					  
		 
		markup = types.InlineKeyboardMarkup(row_width=2)
        	item1 = types.InlineKeyboardButton("Вар1", callback_data='var1')
                item2 = types.InlineKeyboardButton("Вар2", callback_data='var2')
					  
		markup.add(item1, item2)
					  
		bot.send_message(message.chat.id, 'Вариант1', reply_markup=markup)
           else:
                bot.send_message(message.chat.id, 'Вариант2')
			
					  
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'Вар1':
                bot.send_message(call.message.chat.id, 'Ок1')
            elif call.data == 'Вар2':
                bot.send_message(call.message.chat.id, 'Ок2')
 
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выбор",
                reply_markup=None)
 
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="Тест")
 
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
