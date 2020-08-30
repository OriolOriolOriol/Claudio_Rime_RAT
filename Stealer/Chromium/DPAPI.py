
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