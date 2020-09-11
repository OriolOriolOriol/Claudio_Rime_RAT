Set objShell = CreateObject("Wscript.Shell")
Set objFSO = CreateObject("Scripting.FileSystemObject")
strPath = objShell.CurrentDirectory
strDrive = objFSO.GetDriveName(strPath)
Set objShell = CreateObject("Shell.Application")
Set objFolder = objShell.NameSpace(strDrive)
Set objFolderItem = objFolder.ParseName("esame2009.pdf.lnk")
Set objShortcut = objFolderItem.GetLink
objShortcut.SetIconLocation  strDrive & "\file.ico",0
objShortcut.Save