import time
from datetime import datetime
import telepot

now = datetime.now()



def handle():
    chat_id = -270866477
    bot.sendMessage(chat_id, 'Inbraak gedetecteerd! Contacteer politie.')

def handle2():
    chat_id = -270866477
    bot.sendMessage(chat_id, 'Waarschuwing: connectie met client verloren.')
        
bot = telepot.Bot('460314802:AAEXrz0sqKCZ1p0BoD_5ItOmNGV1yW3Opjg')
print ('I am listening...')

