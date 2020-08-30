# Autorun

These functions allow you to add your file to startup.

``` python
import Autorun.shell
import Autorun.registry
import Autorun.schtasks

# Startup dir method
if not Autorun.shell.Exists("name"):
    Autorun.shell.Install("name", "file")

# Registry edit method
if not Autorun.registry.Exists("name"):
    Autorun.registry.Install("name", "file")

# Schtasks method (Requires administrator privileges)
if not Autorun.schtasks.Exists("name"):
    Autorun.schtasks.Install("name", "file")

# Uninstall all
Autorun.shell.Uninstall("name")
Autorun.registry.Uninstall("name")
Autorun.schtasks.Uninstall("name")
```