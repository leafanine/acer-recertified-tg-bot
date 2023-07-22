import telebot
import csv
import urllib.parse
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

BOT_TOKEN=""

bot=telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start','hello'])
def send_welcome(message):
    bot.reply_to(message,"Howdy, how are you doing click /info to get laptop details.")

@bot.message_handler(commands=['info'])
def send_details(message):
    with open("scrapper.py") as f:
        exec(f.read())
        f.close()
    file=open('acer-store.csv')
    csvreader=csv.reader(file)
    header=next(csvreader)
    
    for row in csvreader:
        linker=row[3].replace('"','').strip()
        # print(linker)
        # print(type(linker))
        # linker="https://www.google.com"
        keyboard=InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("More", callback_data="gg", url=linker))
        
        bot.send_message(message.chat.id,text=f'''
                         {row[0]}\n
                         Price: {row[1].replace('"','').replace('â‚¹','INR ')}\n
                         Availability: {row[2].replace('"','')}''',
                         reply_markup=keyboard,
                         )
        
    file.close()
        
    

bot.infinity_polling()