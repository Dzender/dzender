import telebot
import time

bot = telebot.TeleBot("1098107041:AAEXeIq3mrpFsRkBDxDWs7XFw7SQ51oRLzs")

links = []

@bot.message_handler(content_types=['text'])
def function2(message):

	if (message.text.lower()).find("событие без текста") != -1:
		bot.delete_message(message.chat.id, message.message_id)
	elif (message.text).find("https://") != -1:
	    
		text = (message.text)
		text = text.replace('\t', " ")
		text = text.replace('\n', " ")
		list = text.split(" ")

		for i in list:
			#print(list)
			if i.find("https://") != -1 and i.find("Автор:https://") == -1:
				if i not in links:
					links.append(i)
				else:
					bot.delete_message(message.chat.id, message.message_id)

@bot.channel_post_handler(content_types=['text'])
def function2(message):

	if (message.text.lower()).find("событие без текста") != -1:
		bot.delete_message(message.chat.id, message.message_id)
	elif (message.text).find("https://") != -1:
	    
		text = (message.text)
		text = text.replace('\t', " ")
		text = text.replace('\n', " ")
		list = text.split(" ")

		for i in list:
			#print(list)
			if i.find("https://") != -1 and i.find("Автор:https://") == -1:
				if i not in links:
					links.append(i)
				else:
					bot.delete_message(message.chat.id, message.message_id)

		

	time.stop(30)	
	
bot.polling(none_stop=True)

