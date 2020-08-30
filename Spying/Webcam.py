
# Import modules
import os
import urllib.request

__commandCamPATH =  os.path.join(os.getenv("temp"), "CommandCam.exe")
__commandCamLINK = "https://raw.githubusercontent.com/tedburke/CommandCam/master/CommandCam.exe"

""" Create screenshot from webcam """
def Screenshot(filename, delay=4500, camera=1):
    
    # Check if CommandCam.exe exists
    if not os.path.exists(__commandCamPATH):
        urllib.request.urlretrieve(__commandCamLINK, __commandCamPATH)

    # Create screenshot
    command = f"@{__commandCamPATH} /filename \"{filename}\" /delay {delay} /devnum {camera} > NUL"
    os.system(command)

Screenshot("webcam.png")