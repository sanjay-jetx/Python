def leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


def day_in_month(year,month):
    days_list=[31,28,31,30,31,30,31,31,30,31,30,31]
    if leap_year(year) and month == 2:
        return 29
    else:
        return days_list[month-1]

month=int(input("enter the month :"))
year=int(input("enter the year :"))
days=day_in_month(year,month)
print(days) 