from email import message
from importlib.resources import contents
from setuptools import Command
import telebot
import os
import shutil
from dotenv import load_dotenv
import re
import subprocess
from datetime import datetime

load_dotenv()
TELEBOT_ID = os.getenv('TELEGRAMBOT')
CMDCLASSIFY = os.getenv('CMDCLASSIFY')
PATHCLASSIFY = os.getenv('PATHCLASSIFY')
GREETINGMESSAGE = os.getenv('GREETINGMESSAGE')

bot = telebot.TeleBot(TELEBOT_ID)


@bot.message_handler(commands=['hello', 'help'])
def send_welcome(message):
    bot.reply_to(message, GREETINGMESSAGE)
    print(GREETINGMESSAGE)
    writeLog("[Success] Reply greeting message to user at ")


@bot.message_handler(commands=['getlog'])
def reply_log(message):
    logtext = readLogText()
    bot.reply_to(message, logtext)


@bot.message_handler(commands=[CMDCLASSIFY])
def delete_file(message):
    deleteFile(), bot.reply_to(message, "Your file has been deleted")
    writeLog("[Success] Requested to delete all file at ")


# @bot.message_handler(commands="servertemp")
# def reply_checktemp(message):
#     temp, msg = check_CPU_temp()
#     bot.reply_to(message, "temperature (" + u'\xb0' + "C): ", temp),


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

# check server temparature on raspberry pi only


# def check_CPU_temp():
#     temp = None
#     err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
#     if not err:
#         m = re.search(r'-?\d\.?\d*', msg)   # a solution with a  regex
#         try:
#             temp = float(m.group())
#         except ValueError:  # catch only error needed
#             pass
#     return temp, msg


def writeLog(logText):
    with open("log.txt", "a") as file:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        content = logText + now + "\n"
        file.write(content)
        file.close()


def readLogText():
    with open("log.txt", 'r') as f:
        logtext = f.read()
        print(logtext)
        return logtext


bot.polling()
