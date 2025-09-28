import datetime

str = "07:05:45 PM"

def check(str):
    time_24 = datetime.datetime.strptime(str, "%I:%M:%S %p").strftime("%H:%M:%S")
    print(time_24)
   
check(str)    