def newerDate(date1, date2):
    '''Input (date1, date2), returns the newerDate'''
    d1, m1, y1 = date1
    d2, m2, y2 = date2
    if(y1<y2):
        return date2
    elif (y1>y2):
        return date1
    else:
        if m1>m2:
            return date1
        elif m1<m2:
            return date2
        else:
            if d1<d2:
                return date2
            else:
                return date1

def isNewer(date1, date2):
    '''Returns True if date1 is newer, otherwise Fasle'''
    date = newerDate(date1, date2)
    if date == date1:
        return True
    else:
        return False