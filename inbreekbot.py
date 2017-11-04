import time
import telepot

chat_id = -270866477

def handle():
    bot.sendMessage(chat_id, 'Inbraak gedetecteerd! Contacteer politie.')

def handle2():
    bot.sendMessage(chat_id, 'Waarschuwing: connectie met client verloren.')
        
bot = telepot.Bot('460314802:AAEXrz0sqKCZ1p0BoD_5ItOmNGV1yW3Opjg')
print ('Connection with both established')
