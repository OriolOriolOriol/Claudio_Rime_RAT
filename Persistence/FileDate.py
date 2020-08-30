
# Import modules
from os import utime
from time import time as gTime

""" Change file modification time """
def SetModificationTime(path, time):
    return utime(path, (gTime(), time))