
# Import modules
import ctypes

""" Detect debugger """
def Check():
    return ctypes.windll.kernel32.IsDebuggerPresent() != 0