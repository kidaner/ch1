import os
import datetime


def file_date(filename):
    os.getcwd()
    with open(filename, "w") as file:
        pass

    timestamp = os.path.getmtime(file)
    filedate = datetime.datetime.fromtimestamp(timestamp).date()
    filedate.datetimeobj.strftime("%Y-%m-%d")

    return ("{___}".format(filedate)

print(file_date("newfile.txt"))
