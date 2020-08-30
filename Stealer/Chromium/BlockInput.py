
# Import modules
from ctypes import windll
from time import sleep

"""
Block keyboard & mouse
Admin rights is required.
"""
def Block(seconds):
    windll.user32.BlockInput(True)
    sleep(seconds)
    windll.user32.BlockInput(False)