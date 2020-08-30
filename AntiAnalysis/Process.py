
# Import modules
import subprocess

""" Get process list """
def List():
    processes = []
    process = subprocess.check_output("@chcp 65001 1> NUL && @TASKLIST /FI \"STATUS eq RUNNING\" | find /V \"Image Name\" | find /V \"=\"",
        shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
    for processNames in process.split(' '):
        if ".exe" in processNames:
            proc = processNames.replace("K\r\n", '').replace("\r\n", '')
            processes.append(proc)
    return processes

""" Detect blacklisted processes """
def Check():
    # List
    blacklisted_processes = (
        "filemon.exe",
        "regmon.exe",
        "dbgview.exe",
        "diskmon.exe",
        "windbg.exe",
        "ollydbg.exe",
        "procmon.exe",
        "immunitydebugger.exe",
        "wireshark.exe",
        "x32dbg.exe",
        "x64dbg.exe",
    )
    for process in List():
        if process.lower() in blacklisted_processes:
            return True

    return False

Check()