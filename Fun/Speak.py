
# Import modules
import win32com.client as __wincl # pip install pywin32
__sapi = __wincl.Dispatch("SAPI.SpVoice")

""" Say text """
def Speak(text):
    return __sapi.Speak(text)