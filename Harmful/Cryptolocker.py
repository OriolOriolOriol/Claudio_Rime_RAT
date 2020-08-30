
# Import modules
from os import path, walk, remove
from pyAesCrypt import encryptFile, decryptFile # pip install pyAesCrypt

""" Scan files in directory """
def _Scan(dir):
    filelist = []
    for root, _, files in walk(dir):
        for file in files:
            filelist.append(path.join(root, file))
    return filelist

""" Cryptor class """
class Cryptor:
    # Constructor
    def __init__(self, key, bufferSize=64*1024, extension="aes"):
        self.key = key
        self.buffer = bufferSize
        self.extension = extension
    # Encrypt file
    def EncryptFile(self, file):
        if file.endswith('.' + self.extension):
            return
        output = f"{file}.{self.extension}"
        encryptFile(file, output, self.key, self.buffer)
        remove(file)
    # Decrypt file
    def DecryptFile(self, file):
        if not file.endswith('.' + self.extension):
            return
        output = file.replace(self.extension, '')
        decryptFile(file, output, self.key, self.buffer)
        remove(file)
    # Encrypt all files in directory
    def EncryptDir(self, dir):
        files = _Scan(dir)
        for file in files:
            self.EncryptFile(file)
    # Decrypt all files in directory
    def DecryptDir(self, dir):
        files = _Scan(dir)
        for file in files:
            self.DecryptFile(file)