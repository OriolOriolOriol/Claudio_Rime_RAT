
# Import modules : pip install pywin32
from win32api import EnumDisplayDevices, EnumDisplaySettings, ChangeDisplaySettingsEx
from win32con import ENUM_CURRENT_SETTINGS, DMDO_DEFAULT, DMDO_90, DMDO_180, DMDO_270

# Rotations table
__rotations = {
    "0": DMDO_DEFAULT,
    "90": DMDO_90,
    "180": DMDO_180,
    "270": DMDO_270
}

""" Rotate screen """
def Rotate(degrees="0"):
    try:
        rotation_value = __rotations[degrees]
    except KeyError:
        rotation_value = DMDO_DEFAULT
    device = EnumDisplayDevices(None, 0)
    dm = EnumDisplaySettings(device.DeviceName, ENUM_CURRENT_SETTINGS)
    if (dm.DisplayOrientation + rotation_value) % 2 == 1:
        dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
    dm.DisplayOrientation = rotation_value
    ChangeDisplaySettingsEx(device.DeviceName,dm)