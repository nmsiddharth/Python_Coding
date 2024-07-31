year = int(input("Enter Year"))
def leap_year(year):
    if year%4==0 and (year%400==0 or year%100!=0):
        print(year,"is Leap year")
    else:
        print(year, "is not Leap year")

leap_year(year)