import telebot
import os
import shutil
from dotenv import load_dotenv

load_dotenv()
TELEBOT_ID = os.getenv('TELEGRAMBOT')
CMDCLASSIFY = os.getenv('CMDCLASSIFY')
PATHCLASSIFY = os.getenv('PATHCLASSIFY')
MESSAGE = os.getenv('MESSAGE')

bot = telebot.TeleBot(TELEBOT_ID)


@bot.message_handler(commands=['hello', 'help'])
def send_welcome(message):
    bot.reply_to(message, MESSAGE)


@bot.message_handler(commands=[CMDCLASSIFY])
def delete_file(message):
    deleteFile(), bot.reply_to(message, "Your file has been deleted"),


def deleteFile():
    folder = PATHCLASSIFY
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
        return


bot.polling()
