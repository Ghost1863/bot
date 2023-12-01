import telebot
from telebot import types
import webbrowser

bot =telebot.TeleBot('6828222702:AAF_wyVjB69bY2BIFw4KVJnSBQAh57sqYn4')

@bot.message_handler(commands=['start'])
def start(message):
    mark_up= types.ReplyKeyboardMarkup()
    button1 = types.KeyboardButton('Check out this site')
    mark_up.row(button1)
    button2 = types.KeyboardButton('Delete the photo')
    button3 = types.KeyboardButton('Change the photo')
    mark_up.row(button2,button3)
    file=open('rock.jpeg', 'rb')
    bot.send_photo(message.chat.id,file,reply_markup=mark_up)
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}',reply_markup=mark_up)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text=='Check out this site':
        bot.send_message(message.chat.id,'Site is opened!!!')
    elif message.text=='Delete the photo':
        bot.send_message(message.chat.id, 'Photo is deleted!!!')

@bot.message_handler(commands=['main','hi'])#декораторы
def main(message):
    bot.send_message(message.chat.id,f'Your name is {message.from_user.first_name}')
@bot.message_handler(commands=['site','website'])
def site(message):
    webbrowser.open('https://github.com/dashboard')
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, ' <b><u>do not deserve help</u></b>',parse_mode='html')
@bot.message_handler()
def info(message):
    if message.text.lower()=='hi':
        bot.send_message(message.chat.id,f'hello {message.from_user.first_name}')
    elif message.text.lower()=='id':
        bot.reply_to(message,f'It is your id {message.from_user.id}')

@bot.message_handler(content_types=['photo','audio'])
def get_photo(message):
    mark_up=types.InlineKeyboardMarkup()
    button1=types.InlineKeyboardButton('Check out this site',url='https://sites.google.com/view/intdx/%D0%BB%D0%B8%D1%82%D0%B5%D1%80%D0%B0%D1%82%D1%83%D1%80%D0%B0#h.qxop0bhkl68g')
    button2=types.InlineKeyboardButton('Delete the photo',callback_data='delete')
    button3=types.InlineKeyboardButton('Change the photo',callback_data='edit')
    mark_up.row(button1,button2,button3)
    bot.reply_to(message,'It is absolutely fantastic',reply_markup=mark_up)

@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data== 'delete':
        bot.delete_message(callback.message.chat.id,callback.message.message_id-1)
    elif callback.data=='edit':
        bot.edit_message_text('Edit',callback.message.chat.id,callback.message.message_id)
bot.polling(none_stop=True)
