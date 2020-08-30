
# Import modules
import os.path
from os import remove

__startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft\\Windows\\Start Menu\\Programs\\Startup")

""" Add to startup (startup dir) """
def Install(name, executable):
    payload = (f"""
    [InternetShortcut]
    URL=file://{os.path.abspath(executable)}
    """)
    target = os.path.join(__startup_path, name + ".url")
    with open(target, 'w') as file:
        file.write(payload)

    return True

""" Delete from startup (startup dir) """
def Uninstall(name):
    target = os.path.join(__startup_path, name + ".url")
    try: remove(target)
    except FileNotFoundError:
        pass
    return not os.path.exists(name)

""" Check if exists (startup dir) """
def Exists(name):
    target = os.path.join(__startup_path, name + ".url")
    return os.path.exists(target)