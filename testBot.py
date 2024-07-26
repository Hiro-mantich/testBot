import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6773015806:AAGmS-0vR5KRekrLDmYBgbCQ5PIXTx7HtUs')
###
@bot.message_handler(commands = ['stop'])
def stop_Bot(message):
    bot.send_message(message.chat.id, 'Бот выключен!\nПока!')


@bot.message_handler(commands = ['start'])
def start_Bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1= types.KeyboardButton('Актуальные акции')
    btn2=types.KeyboardButton('Список активистов')
    btn3=types.KeyboardButton('Положение профкома')
    btn4 =types.KeyboardButton('Всё о стипендиях')
    btn5 =types.KeyboardButton('Задать вопрос')
    btn6=types.KeyboardButton('Перейти в канал(группу)')
    markup.row(btn1)
    markup.row(btn2,btn3)
    markup.row(btn4, btn5)
    markup.row(btn6)

    bot.send_message(message.chat.id, 'Бот запущен!\nПривет, {0.first_name}!'.format(message.from_user), reply_markup=markup)

   # bot.register_next_step_handler(message,btn_click)

@bot.message_handler(content_types=['text'])
def menu(message):
    if message.text == 'Перейти в канал(группу)':
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton('Перейти', url='https://vk.com/pposaltstu')
        markup.add(btn)
        bot.send_message(message.chat.id, 'Нажмите кнопку ниже, чтобы перейти в канал(группу):', reply_markup=markup)
    elif message.text == 'Список активистов':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton('Председатель ППОС')
        item2 = types.KeyboardButton('Специалист ППОС')
        item3 = types.KeyboardButton('Специалист ППОС')
        item4 = types.KeyboardButton('Председатель профбюро')
        btn_back = types.KeyboardButton('⬅Назад')

        markup.row(item1)
        markup.row(item2)
        markup.row(item3)
        markup.row(item4)
        markup.row(btn_back)
       # markup.add(item1,item2,item3,item4,btn_back)

        bot.send_message(message.chat.id, 'Список активистов', reply_markup = markup)
    elif message.text == '⬅Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Актуальные акции')
        btn2 = types.KeyboardButton('Список активистов')
        btn3 = types.KeyboardButton('Положение профкома')
        btn4 = types.KeyboardButton('Всё о стипендиях')
        btn5 = types.KeyboardButton('Задать вопрос')
        btn6 = types.KeyboardButton('Перейти в канал(группу)')
        markup.row(btn1)
        markup.row(btn2, btn3)
        markup.row(btn4, btn5)
        markup.row(btn6)

        bot.send_message(message.chat.id, '⬅Назад'.format(message.from_user), reply_markup=markup)



bot.polling(none_stop=True)