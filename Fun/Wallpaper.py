
# Import modules
from ctypes import windll
from os import path
__SPI_SETDESKWALLPAPER = 20 

""" Get screen resolution x, y """
def GetScreenResolution():
    x = windll.user32.GetSystemMetrics(0)
    y = windll.user32.GetSystemMetrics(1)
    return (x, y)

""" Set desktop wallpaper """
def Set(image):
    # Check path
    if not path.exists(image):
        raise FileNotFoundError(f"Image {repr(image)} not exists")
    # Get absolute path
    image = path.abspath(image)
    # Set
    return windll.user32.SystemParametersInfoW(__SPI_SETDESKWALLPAPER, 0, image, 3)