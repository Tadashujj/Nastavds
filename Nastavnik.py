import telebot
from telebot import types
bot=telebot.TeleBot("6697732049:AAF1_m6cV8wZ1-20h_bdOUJoUxSCCGE4MOo")
@bot.message_handler(commands=['curator'])
def chat(chat):
    
        use=types.InlineKeyboardMarkup()
        btn1=types.InlineKeyboardButton(text='Benjamin ⚡️', url='https://t.me/BenjamimDirector')
        btn2=types.InlineKeyboardButton(text='Qweef ⚡️',url='https://t.me/cabjah')
        btn3=types.InlineKeyboardButton(text='Соня Мармеладова ⚡️', url='https://t.me/president14888')
        use.add(btn1)
        use.add(btn2)
        use.add(btn3)
        bot.send_message(chat.chat.id,'Нехватает навыков СИ ? \n\
    выбирай себе наставника и вперед за работу !', reply_markup=use)
bot.polling(none_stop=True)    