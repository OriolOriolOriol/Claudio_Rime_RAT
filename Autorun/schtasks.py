
# Import modules
import os.path
import subprocess

__schtasks = "@chcp 65001 && @schtasks.exe"

""" Add to startup (schtasks) """
def Install(name, executable):
    try:
        process = subprocess.check_output(f"{__schtasks} /create /f /sc ONLOGON /RL HIGHEST /tn \"{name}\" /tr \"{os.path.abspath(executable)}\"",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return "SUCCESS:" in process

""" Delete from startup (schtasks) """
def Uninstall(name):
    try:
        process = subprocess.check_output(f"{__schtasks} /delete /f /tn \"{name}\"",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return "SUCCESS:" in process

""" Check if exists (schtasks) """
def Exists(name):
    try:
        process = subprocess.check_output(f"{__schtasks} /query /tn \"{name}\"",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return not "ERROR:" in process