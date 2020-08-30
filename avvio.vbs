Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("Wscript.Shell")
strPath = objShell.CurrentDirectory
strDrive = objFSO.GetDriveName(strPath)
Dim strArgs
strArgs = "cmd /c" & " " & strDrive & "\python\python.exe" & " "  & strDrive & "\CrazyPy\Run\Run\bin\Debug\netcoreapp3.1\Carlos.pyw"
objShell.Run strArgs, 0, false