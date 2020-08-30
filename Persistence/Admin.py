
# Import modules
from ctypes import windll

""" Is user administrator """
def IsAdministrator():
    return windll.shell32.IsUserAnAdmin() != 0

""" Run files as administrator """
def RunAsAdmin(executable, params=''):
    return windll.shell32.ShellExecuteW(None, "runas", executable, params, None, 1)