
# Import modules
from json import loads
from urllib.error import URLError
from urllib.request import urlopen

""" Organizations list """
__organizations = (
    "microsoft",
    "google",
    "amazon",
    "facebook",
    "avast",
    "avira",
    "avg",
    "vds",
    "cisco",
    "bitdefender",
    "comodo",
    "clamwin",
    "dr.web",
    "eset",
    "grizzly",
    "kaspersky",
    "malware",
    "norton",
    "antivirus",
    "security",
    "secure",
    "defender",
    "zonealarm",
    "immunet",
    "check point",
    "f-secure",
    "f-prot",
    "frisk",
    "fortinet",
    "g data",
    "mcaffe",
    "sophos",
    "panda",
    "qihoo",
    "quick heal",
    "trend micro",
    "trustport",
    "virusblokada",
    "webroot",
    "symantec",
)

""" Detect Antivirus organization by ip """
def Check(ip=''):
    try:
        result = urlopen(f"http://ip-api.com/json/{ip}").read().decode('utf8')
    except URLError:
        pass
    else:
        isp = loads(result)["isp"].lower()
        for organization in __organizations:
            if isp in organization:
                return True
    
    return False