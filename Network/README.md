# Network functions

``` python
import Network.Whois
import Network.NetDiscover

# Get basic IP address information
Network.Whois.Info(ip="8.8.8.8")
# Get geo data by ip address
Network.Whois.Geoplugin(ip="8.8.8.8")
# Get coordinates by bssid address
Network.Whois.GetLocationByBSSID(bssid="A0:F3:C1:3B:6F:90")

# Get router ip
print("Router address : " + str(Network.NetDiscover.GetDefaultGateway()))
# Ping all ip addresses from {start} to {stop}
# and return the list of active.
Network.NetDiscover.ScanNetwork(start=1, stop=256)
Network.NetDiscover.PortIsOpen(ip="8.8.8.8", port=80) # True / False
# Return mac by ip
Network.NetDiscover.GetMacByIP("192.168.1.1")
```