
# Import modules
import os.path
import subprocess


__registry = "@chcp 65001 && @reg.exe"
__autorun_key = "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"

""" Add to startup (registry) """
def Install(name, executable):
    try:
        process = subprocess.check_output(f"{__registry} ADD {__autorun_key} /V \"{name}\" /t REG_SZ /F /D \"{os.path.abspath(executable)}\"",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return "successfully" in process

""" Delete from startup (registry) """
def Uninstall(name):
    try:
        process = subprocess.check_output(f"{__registry} DELETE {__autorun_key} /V \"{name}\" /F",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return "successfully" in process

""" Check if exists (registry) """
def Exists(name):
    try:
        process = subprocess.check_output(f"{__registry} QUERY {__autorun_key} /v \"{name}\"",
            shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    except subprocess.CalledProcessError:
        return False
    else:
        return not "ERROR:" in process