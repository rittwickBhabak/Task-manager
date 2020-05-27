from getNextOrPreviousDay import nextDay

def getDates(list_of_intervals, starting_date):
    '''Return dates in the specific interval from the starting date'''
    myList = list_of_intervals
    dates = []
    d, m, y = starting_date
    for day in myList:
        for i in range(day):
            d, m, y = nextDay(d,m,y)
        dates.append([d,m,y])
    return dates