
# Import modules
from ctypes import windll, wintypes, create_unicode_buffer, WINFUNCTYPE, Structure, c_bool, c_int, c_long, c_ulong, byref, POINTER
from psutil import process_iter, Process # pip install psutil

__user32 = windll.user32
__EnumWindows = __user32.EnumWindows
__EnumWindowsProc = WINFUNCTYPE(c_bool, POINTER(c_int), POINTER(c_int))
__IsWindowVisible = __user32.IsWindowVisible
__GetWindowThreadProcessId = __user32.GetWindowThreadProcessId

""" Get Window object by process """
def GetWindowByProcess(processName):
    for proc in process_iter():
        if processName in proc.name():
            pid = proc.pid
            name = proc.name()
            try:
                hwnd = __FindHwndNyPid(pid)
            except IndexError:
                continue
            else:
                return __Window(pid, name, hwnd)
    return False

""" Get PID by hwnd """
def __GetPidByHWND(hwnd):
    pid = wintypes.DWORD()
    __GetWindowThreadProcessId(hwnd, byref(pid))
    return pid.value

""" Get hwnd by PID """
def __FindHwndNyPid(pid):
    hwnds = []
    def foreach_window(hwnd, lParam):
        if __IsWindowVisible(hwnd):
            if __GetPidByHWND(hwnd) == pid:
                hwnds.append(hwnd)
        return True
    __EnumWindows(__EnumWindowsProc(foreach_window), 0)
    return hwnds[0]

""" Rect """
class Rect(Structure):
    _fields_ = [
        ('left', c_long),
        ('top', c_long),
        ('right', c_long),
        ('bottom', c_long)
    ]

""" Window class """
class __Window:
    # Constructor
    def __init__(self, pid, name, hwnd):
        __rect = wintypes.RECT()
        self.pid = pid
        self.hwnd = hwnd
        self.name = name
        self.__user32 = windll.user32
        self.__user32.GetWindowRect(self.hwnd, byref(__rect))
        self.rect = Rect(__rect.left, __rect.top, __rect.right, __rect.bottom)
    # Representation
    def __repr__(self):
        return f"Window (pid={self.pid}, name={repr(self.name)})"
    # Maximize window
    def Maximize(self):
        return self.__user32.ShowWindow(self.hwnd, 3)
    # is Maximized
    def isMaximized(self):
        return self.__user32.IsZoomed(self.hwnd) != 0
    # Minimize window
    def Minimize(self):
        return self.__user32.ShowWindow(self.hwnd, 6)
    # is Minimized
    def isMinimized(self):
        return self.__user32.IsIconic(self.hwnd) != 0
    # Restore window
    def Restore(self):
        return self.__user32.ShowWindow(self.hwnd, 9)
    # Activate window
    def Activate(self):
        return self.__user32.SetForegroundWindow(self.hwnd)
    # Move window
    def Move(self, x, y, height, width, repaint=True):
        return self.__user32.MoveWindow(self.hwnd, x, y, height, width, repaint)
    # Get title
    def Title(self):
        textLenInCharacters = self.__user32.GetWindowTextLengthW(self.hwnd)
        stringBuffer = create_unicode_buffer(textLenInCharacters + 1)
        self.__user32.GetWindowTextW(self.hwnd, stringBuffer, textLenInCharacters + 1)
        return stringBuffer.value
    # Get executable location
    def Executable(self):
        p = Process(self.pid)
        return p.exe()
    # Close window
    def Close(self):
        return self.__user32.PostMessageA(self.hwnd, 0x0010, 0, 0)
    # Kill process
    def Terminate(self):
        p = Process(self.pid)
        return p.terminate()
    # is Visible
    def isVisible(self):
        return self.__user32.IsWindowVisible(self.hwnd) != 0