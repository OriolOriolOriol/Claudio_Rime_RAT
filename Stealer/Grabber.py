
# Import modules
import os
import zipfile

""" Scan files in directory """
def Scan(path):
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            filelist.append(os.path.join(root, file))
    return filelist

""" Grab files from directory to archive """
def Grab(path, archivePath="grab.zip", maxsize=5242880, extensions=[]):
    with zipfile.ZipFile(archivePath, 'w', zipfile.ZIP_DEFLATED) as archive:
        files = Scan(path)
        for file in files:
            # Check size
            if os.stat(file).st_size > maxsize:
                continue
            # Check extension
            extension = file.split('.')[-1]
            if len(extensions) > 0 and not extension in extensions:
                continue
            # Write file to archive
            archive.write(file)

    return archivePath