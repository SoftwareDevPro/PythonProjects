
import calendar
import pyfiglet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-y','--year',help='the year')
parser.add_argument('-m','--month',help='the month')
args = parser.parse_args()

year = int(args.year)
month = int(args.month)

month_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# display the calendar
month_str = pyfiglet.figlet_format(month_dict[month])
print(month_str) 
print(calendar.month(year, month))



