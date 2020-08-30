
# Import modules
from ctypes import windll

"""
Set attrib hidden to file
The file or directory is hidden.
It is not included in an ordinary directory listing. 
"""
def SetHidden(path):
    return windll.kernel32.SetFileAttributesW(path, 0x02)

"""
Set attrib system to file.
A file or directory that the operating system uses a part of,
or uses exclusively.
"""
def SetSystem(path):
    return windll.kernel32.SetFileAttributesW(path, 0x04)

"""
Set attrib normal to file.
A file that does not have other attributes set.
This attribute is valid only when used alone. 
"""
def SetNormal(path):
    return windll.kernel32.SetFileAttributesW(path, 0x80)