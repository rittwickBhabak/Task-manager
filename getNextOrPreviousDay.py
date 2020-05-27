def isLeapYear(year):
    '''Returns true if leap year'''
    if (year%100!=0 and year%4==0) or (year%400==0):
        return True
    return False

def last_date_of_month(month, year):
    '''Month should be an integer 1 to 12'''
    try:
        month = int(month)
        if month==2 and isLeapYear(year):
            return 29
        elif month==2:
            return 28
        elif month in [1,3,5,7,8,10,12]:
            return 31
        else:
            return 30
    except Exception as e:
        print('Some error occured, error is --> ', e)

def nextDay(day, month, year):
    '''Return next day of given date (day,month,year)'''
    last_date = last_date_of_month(month, year)
    if not day==last_date:
        return day+1, month, year
    elif not month==12:
        return 1, month+1, year
    else:
        return 1, 1, year + 1

def previousDay(day, month, year):
    '''Return previous day of give date (day, month, year)'''
    if not day==1:
        return day-1, month, year
    elif not month==1:
        return last_date_of_month(month-1, year), month-1, year
    else:
        return 31, 12, year - 1
