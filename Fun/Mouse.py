
# Import modules
from ctypes import windll, Structure, c_long, byref

class __POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]

""" Get cursor position """
def GetPosition():
    pt = __POINT()
    windll.user32.GetCursorPos(byref(pt))
    return (pt.x, pt.y)

""" Set cursor position """
def SetPosition(x, y):
    windll.user32.SetCursorPos(x, y)

""" Make click """
def Click():
    windll.user32.mouse_event(2, 0, 0, 0,0)
    windll.user32.mouse_event(4, 0, 0, 0,0)