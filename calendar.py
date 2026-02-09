import datetime
import time
import os
import math
import json

class Format:
    end = '\033[0m'
    underline = '\033[4m'

date_and_time = datetime.datetime.now()

year = date_and_time.strftime("%Y")

month_string = date_and_time.strftime("%B")
month_int = int(date_and_time.strftime("%m"))

day = date_and_time.strftime("%d")


def getfirstof(m):
    first_of = datetime.datetime(int(year), m, 1)
    return first_of

start_time = time.time()
framesecond = 1

def clear():
    os.system('clear')


# displays the top of the calendar with the month and week days
def displaystart():
    clear()

    print(date_and_time)

    print("_____________________________________________")
    
    ascii_art = '''{
  "1": "     _                             \\n  _ | |__ _ _ _ _  _ __ _ _ _ _  _ \\n | || / _` | ' \\\\ || / _` | '_| || |\\n  \\\\__/\\\\__,_|_||_\\\\_,_\\\\__,_|_|  \\\\_, |\\n                               |__/ ",
  "2": "  ___    _                           \\n | __|__| |__ _ _ _  _ __ _ _ _ _  _ \\n | _/ -_) '_ \\\\ '_| || / _` | '_| || |\\n |_|\\\\___|_.__/_|  \\\\_,_\\\\__,_|_|  \\\\_, |\\n                                |__/ ",
  "3": "  __  __             _    \\n |  \\\\/  |__ _ _ _ __| |_  \\n | |\\\\/| / _` | '_/ _| ' \\\\ \\n |_|  |_\\\\__,_|_| \\\\__|_||_|\\n                          ",
  "4": "    _            _ _ \\n   /_\\\\  __ _ _ _(_) |\\n  / _ \\\\/ _` | '_| | |\\n /_/ \\\\_\\\\__, |_| |_|_|\\n          |_|        ",
  "5": "  __  __           \\n |  \\\\/  |__ _ _  _ \\n | |\\\\/| / _` | || |\\n |_|  |_\\\\__,_|\\\\_, |\\n              |__/ ",
  "6": "     _               \\n  _ | |_  _ _ _  ___ \\n | || | || | ' \\\\/ -_)\\n  \\\\__/ \\\\_,_|_||_\\\\___|\\n                     ",
  "7": "     _      _      \\n  _ | |_  _| |_  _ \\n | || | || | | || |\\n  \\\\__/ \\\\_,_|_|\\\\_, |\\n              |__/ ",
  "8": "    _                    _   \\n   /_\\\\ _  _ __ _ _  _ __| |_ \\n  / _ \\\\ || / _` | || (_-<  _|\\n /_/ \\\\_\\\\_,_\\\\__, |\\\\_,_/__\\\\__|\\n           |___/             ",
  "9": "  ___           _             _             \\n / __| ___ _ __| |_ ___ _ __ | |__  ___ _ _ \\n \\\\__ \\\\/ -_) '_ \\\\  _/ -_) '  \\\\| '_ \\\\/ -_) '_|\\n |___/\\\\___| .__/\\\\__\\\\___|_|_|_|_.__/\\\\___|_|  \\n          |_|                               ",
  "10": "   ___     _       _             \\n  / _ \\\\ __| |_ ___| |__  ___ _ _ \\n | (_) / _|  _/ _ \\\\ '_ \\\\/ -_) '_|\\n  \\\\___/\\\\__|\\\\__\\\\___/_.__/\\\\___|_|  \\n                                 ",
  "11": "  _  _                   _             \\n | \\\\| |_____ _____ _ __ | |__  ___ _ _ \\n | .` / _ \\\\ V / -_) '  \\\\| '_ \\\\/ -_) '_|\\n |_|\\\\_\\\\___/\\\\_/\\\\___|_|_|_|_.__/\\\\___|_|  \\n                                       ",
  "12": "  ___                   _             \\n |   \\\\ ___ __ ___ _ __ | |__  ___ _ _ \\n | |) / -_) _/ -_) '  \\\\| '_ \\\\/ -_) '_|\\n |___/\\\\___\\\\__\\\\___|_|_|_|_.__/\\\\___|_|                                   "
}'''

    data = json.loads(ascii_art)

    print(data[str(month_int)])
    print("    -----------------------------------")   
    print("      M    T    W    T    F    S    S")
    print("    -----------------------------------")    

spacer = "-"
def displaydates():
    rows = []
    daysOfDate = 0
    spacer_amount = 0
    selectedmonth = month_int

    for y in range(1, 6):
        week_count = 0
        days_count = 0
        rows = []
        for x in range(1, 8):
            if spacer_amount == getfirstof(selectedmonth).weekday():
                if days_count <= 7 and daysOfDate < 31:
                    daysOfDate += 1
                    if daysOfDate >= 10:
                        string_dd = str(daysOfDate) + "  "
                    else:
                        string_dd = str(daysOfDate) + "   "
                    rows.insert(x, string_dd)
            else:
                if daysOfDate >= 10:
                    string_dd = str(spacer) + "  "
                else:
                    string_dd = str(spacer) + "   "
                rows.insert(x, string_dd)
                spacer_amount += 1

        string_rows = " ".join(rows)
        print("      " + string_rows)

        week_count += 1


displaystart()

displaydates()

print("starting..")

while True:
    if (time.time() - start_time) > framesecond :
        displaystart()
        displaydates()
        start_time = time.time()
