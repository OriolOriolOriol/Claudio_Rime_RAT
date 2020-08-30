
# Import modules
from ctypes import windll, create_unicode_buffer, WINFUNCTYPE, c_bool, c_int, POINTER

""" Get active window title """
def Get():
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    if buf.value:
        return buf.value
    else:
        return None

ciao=Get()
print(ciao)

""" Get all windows titles """
def GetAll():
    EnumWindows = windll.user32.EnumWindows
    EnumWindowsProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
    GetWindowText = windll.user32.GetWindowTextW
    GetWindowTextLength = windll.user32.GetWindowTextLengthW
    IsWindowVisible = windll.user32.IsWindowVisible
    titles = []
    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            if buff.value:
                titles.append(buff.value)
        return True
    EnumWindows(EnumWindowsProc(foreach_window), 0)
    return titles 
