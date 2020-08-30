
# All key codes
# http://help.openspan.com/191/adapters_interrogation/key_codes_for_sendkeys_method.htm

# Import modules
from os import system

""" Send key press """
def SendKeys(text):
    command = f"""
    @powershell.exe Add-Type -AssemblyName System.Windows.Forms;
    [System.Windows.Forms.SendKeys]::SendWait({repr(text)});
    """
    return system(command) == 0