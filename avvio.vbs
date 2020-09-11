Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("Wscript.Shell")
strPath = objShell.CurrentDirectory
strDrive = objFSO.GetDriveName(strPath)
Dim strArgs
Dim strArgs2
strArgs2 = "cmd /c" & " " & strDrive & "\prova.vbs"
strArgs = "cmd /c" & " " & strDrive & "\python\python.exe" & " "  & strDrive & "\CrazyPy\Run\Run\bin\Debug\netcoreapp3.1\Carlos.pyw"
objShell.Run strArgs2, 0, false
objShell.Run strArgs, 0, false