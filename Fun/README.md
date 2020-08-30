# Fun functions

``` python
import Fun.Cdrom
import Fun.Keyboard
import Fun.Mouse
import Fun.Speak
import Fun.Screen
import Fun.Url
import Fun.Wallpaper
import Fun.Windows


# Cdrom control
Fun.Cdrom.Open()
Fun.Cdrom.Close()

# Keyboard control
Fun.Keyboard.SendKeys("Hello world{ENTER}")

# Mouse control
x, y = Fun.Mouse.GetPosition()
Fun.Mouse.SetPosition(x + 40, y + 100)
Fun.Mouse.Click()

# Text to speech
Fun.Speak.Speak("Hello world")

# Rotate screen ("0", "90", "180", "270)
Fun.Screen.Rotate("180")

# Open url on browser
Fun.Url.Open("google.com")

# Wallpaper
x, y = Fun.Wallpaper.GetScreenResolution()
Fun.Wallpaper.Set("wallpaper.jpg")

# Work with windows
firefox = Fun.Windows.GetWindowByProcess("firefox.exe")
if firefox == None:
    print("Failed to find firefox process!")
    exit()

print("Window title : " + firefox.Title())
print("Executable path : " + firefox.Executable())
# Minimize window
firefox.Minimize()
# Maximize window
firefox.Maximize()
# Move window: x, y, height, width
firefox.Move(0, 0, 400, 500)

```