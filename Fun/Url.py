
# Import modules
from os import system

""" Open url in default browser """
def Open(url):
    if not url.startswith("http"):
        url = "http://" + url
    return system(f"@start {url} > NUL")
