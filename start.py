import telebot
import os
import shutil

bot = telebot.TeleBot("1107438786:AAED_PIcm4FYHNX_zCLJBGDktDVpAvf7g5Q")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['bkajuyovy'])
def delete_file(message):
    deleteFile(), bot.reply_to(message, "Your file has been deleted"),

def deleteFile():
    folder = '/mnt/NASDrive/Classify'
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