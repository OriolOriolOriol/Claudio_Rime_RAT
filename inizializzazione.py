def processamento():
	import win32com.client
	strComputer = "."
	objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
	objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")

	# 1. Win32_DiskDrive
	colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_DiskDrive WHERE InterfaceType = \"USB\"")
	DiskDrive_DeviceID = colItems[0].DeviceID.replace('\\', '').replace('.', '')
	DiskDrive_Caption = colItems[0].Caption

	# 2. Win32_DiskDriveToDiskPartition
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_DiskDriveToDiskPartition")
	for objItem in colItems:
		if DiskDrive_DeviceID in str(objItem.Antecedent):
			DiskPartition_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')

	# 3. Win32_LogicalDiskToPartition
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDiskToPartition")
	for objItem in colItems:
		if DiskPartition_DeviceID in str(objItem.Antecedent):
			LogicalDisk_DeviceID = objItem.Dependent.split('=')[1].replace('"', '')


	# 4. Win32_LogicalDisk
	colItems = objSWbemServices.ExecQuery("SELECT * from Win32_LogicalDisk WHERE DeviceID=\"" + LogicalDisk_DeviceID + "\"")
	print()

	return str(LogicalDisk_DeviceID)


disco = processamento()
disco=disco+"\\"
with open("disco.txt","w") as file:
	file.write(disco)
