import telebot
from telebot import types
from fractions import Fraction

API_TOKEN = '1176241014:AAGO12D0urL9ATkc-Juejqoq-WCplbOKaL8'

bot = telebot.TeleBot(API_TOKEN)

Viki = 1000947005
Kate = 1000947005
Alex = 301146859
chat_id = Alex

#bot.send_message(Viki, "Привет)))))))")

# @bot.message_handler(content_types=['text'])
# def lalala(message):
#     bot.send_message(chat_id, f"{message.text}\n\nFrom: {message.from_user.first_name} \nId: {message.from_user.id}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Пока ты можешь только складывать простые дроби и находить проценты')
    bot.send_message(message.chat.id, 'Узнать правила: /help \nНачать пользоваться: /count')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, так и знал, что нажмешь ХЕЛП.'
                                      f'\nКороче:'
                                      f'\nСначала ставим палочку: /'
                                      f'\nВыбираем /count и пишем по порядку по ОДНОМУ числу'
                                      f'\nДроби указываем в формате: 5/6'
                                      f'\nПроценты: сначала что, потом от чего!')

user_dict = {}

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None


# Handle '/start' and '/help'
@bot.message_handler(commands=['count'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Введите первое число: ")
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        #msg = bot.reply_to(message, 'How old are you?')
        msg = bot.send_message(message.chat.id, "Введите второе число: ")
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        # if not age.isdigit():
        #     msg = bot.reply_to(message, 'Age should be a number. How old are you?')
        #     bot.register_next_step_handler(msg, process_age_step)
        #     return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
        markup.add('Сложить', 'Процент')
        msg = bot.reply_to(message, 'Чё делать?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_sex_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        if (sex == u'Сложить'):
            x = Fraction(str(user.name)) + Fraction(str(user.age))
            bot.send_message(chat_id, x)
        elif (sex == u'Процент'):
            x = int(user.name)/int(user.age) * 100
            bot.send_message(chat_id, f"{x} %")
        #bot.send_message(chat_id, x)
        #bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\n Age:' + str(user.age) + '\n Sex:' + user.sex)
        #types.ReplyKeyboardRemove(remove_keyboard=True)
    except Exception as e:
        bot.reply_to(message, 'oooops')


# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
#bot.enable_save_next_step_handlers(delay=1)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
#bot.load_next_step_handlers()

bot.polling()


