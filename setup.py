import telebot
import random

from telebot import types

bot = telebot.TeleBot('1139813975:AAHKEDk-MHU-d2xADVdoArtuZDlnSk3ZOJM')


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '/random':
            bot.send_message(message.chat.id, str(random.randint(0, 100)))

        elif message.text == '/start':
            bot.send_message(message.chat.id, 'Привет,'+ message.from_user.first_name+'!')

        elif message.text == '/kakdela':

            markup = types.InlineKeyboardMarkup(row_width=4)
            item1 = types.InlineKeyboardButton("is doing", callback_data='good')
            item2 = types.InlineKeyboardButton("does", callback_data='bad')
            item3 = types.InlineKeyboardButton("did", callback_data='good_1')
            item4 = types.InlineKeyboardButton("have done", callback_data='bad_1')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id, 'She ... (to do) homework.', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Present Continuous", reply_markup=None)
            elif call.data == 'bad':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Present Simple", reply_markup=None)
            elif call.data == 'good_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Past Simple", reply_markup=None)

            elif call.data == 'bad_1':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                      text="Present Perfect", reply_markup=None)
            # remove inline buttons


            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
