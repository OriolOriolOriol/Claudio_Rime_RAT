 
# Anti Analysis  

The functions allow you to determine whether the running file is located on virtual machines, emulators, debuggers or in the sandbox  

``` python
import AntiAnalysis

Antianalysis.VirtualBox.Check() # True / False
Antianalysis.SandBox.Check() # True / False
Antianalysis.Debugger.Check() # True / False
Antianalysis.Emulator.Check() # True / False
Antianalysis.Organization.Check() # True / False
Antianalysis.Process.Check() # True / False
Antianalysis.Process.List() # Returns a list with active processes
```
