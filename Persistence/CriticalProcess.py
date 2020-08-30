
# Import modules
from ctypes import windll, byref, c_bool

"""
Set process critical.
Admin rights is required.
"""
def Set():
    t = c_bool()
    windll.ntdll.RtlAdjustPrivilege(20, 1, 0, byref(t))
    return windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

"""
Set process not critical.
Admin rights is required.
"""
def Unset():
    return windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0