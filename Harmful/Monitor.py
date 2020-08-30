
# Import modules
from ctypes import windll
import time
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
time.sleep(5)
On()