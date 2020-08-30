
# Import modules
from os import system

def Reboot():
    system('@shutdown /r /t 0')

def Shutdown():
    system('@shutdown /s /t 0')

def Logoff():
    system('@shutdown /l')

def Hibernate():
    system('@shutdown /h')