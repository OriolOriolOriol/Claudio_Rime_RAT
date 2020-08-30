
# Import modules
import os
import re
import uuid
import ctypes
from . import Process

""" Detect virtual box """
def Check():

    # Dll check
    vmware_dll = os.path.join(os.environ["SystemRoot"], "System32\\vmGuestLib.dll")
    virtualbox_dll = os.path.join(os.environ["SystemRoot"], "vboxmrxnp.dll")  
    if os.path.exists(virtualbox_dll) or os.path.exists(vmware_dll):
        return True

    # Registry check
    reg0 = "REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\"
    reg1 = os.system(f"{reg0}DriverDesc 2> nul")
    reg2 = os.system(f"{reg0}ProviderName 2> nul")
    if reg1 != 1 and reg2 != 1:    
        return True

    # List
    virtualbox_processes = (
        "vboxservice.exe", "vboxtray.exe",
        "vmtoolsd.exe", "vmwaretray.exe", "vmwareuser", "VGAuthService.exe",
        "vmacthlp.exe", "vmsrvc.exe", "vmusrvc.exe",
        "prl_cc.exe", "prl_tools.exe",
        "xenservice.exe", "qemu-ga.exe",
        "joeboxcontrol.exe", "joeboxserver.exe", "joeboxserver.exe"
    )
    # Process check
    for process in Process.List():
        if process.lower() in virtualbox_processes:
            return True
    
    # Mac adderess check
    mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    vmware_mac_list = ("00:05:69", "00:0c:29", "00:1c:14", "00:50:56")
    if mac_address[:8] in vmware_mac_list:
        return True

    # Screen size check
    x = ctypes.windll.user32.GetSystemMetrics(0)
    y = ctypes.windll.user32.GetSystemMetrics(1)
    if x <= 200 or y <= 200:
        return True

    return False