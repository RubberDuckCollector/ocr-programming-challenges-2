from datetime import date
from datetime import datetime as dt

def today():
    time = dt.now().strftime("%H:%M:%S")
    print(f"Today is {date.today().strftime('%A %d %B %Y')} at {time}") # type: ignore

date = input("Enter a date (yyyy-mm-dd): ")
date = dt.strptime(date, "%Y-%m-%d")
print(date)
print(dt.strftime(date, "%A"))


# today()