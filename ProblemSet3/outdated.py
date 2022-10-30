# September 8, 1636
# 9/8/1636
# month date year format input
import re

months_list= [ 
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December" ]

while True:
    try:
        date = input("Month:")
        date_list = re.split(", | |/",date)
        print(date_list)
        month = date_list[0]
        try:
            month = int(month)
        except:
            month = int(months_list.index(month) + 1)
        day = int(date_list[1])
        year = int(date_list[2])
        
        if day > 31:
            print("Invalid date")
        elif month < 1 or month > 12:
            continue
        else:
            print(f"{year}-{month}-{day}")
            break
    except ValueError:
        print("Invalid month")
        break
    else:
        continue

