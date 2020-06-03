from dateComparator import isNewer
from getDatesInSpecificInterval import getDates 
from getNextOrPreviousDay import nextDay, last_date_of_month

def getRepDates(repList,sdate,edate):
    # repList = { "0":0, "1":2, "2":2, "3":2, "5":2, "7":4, "10":2, "15":0, "20":0, "30":0, "45":0, "60":0, "90":0, "120":0, "180":0, "360":0}
    # sdate = (1,2,2020)
    # edate = (last_date_of_month(12,2020),12,2020)
    pdate = sdate
    dates = []
    forverInterval = None
    if repList["0"]>0:
        while not isNewer(pdate, edate):
            dates.append(pdate)
            for i in range(repList["0"]):
                pdate = nextDay(pdate[0],pdate[1],pdate[2])
    else:
        tempList = [repList["1"],repList["2"],repList["3"],repList["5"],repList["7"],repList["10"],repList["15"],repList["20"],repList["30"],repList["45"],repList["60"],repList["90"],repList["120"],repList["180"],repList["360"]]
        myList = []
        for i in range(repList['1']):
            myList.append(1)
        for i in range(repList['2']):
            myList.append(2)
        for i in range(repList['3']):
            myList.append(3)
        for i in range(repList['5']):
            myList.append(5)
        for i in range(repList['7']):
            myList.append(7)
        for i in range(repList['10']):
            myList.append(10)
        for i in range(repList['15']):
            myList.append(15)
        for i in range(repList['20']):
            myList.append(20)
        for i in range(repList['30']):
            myList.append(30)
        for i in range(repList['45']):
            myList.append(45)
        for i in range(repList['60']):
            myList.append(60)
        for i in range(repList['90']):
            myList.append(90)
        for i in range(repList['120']):
            myList.append(120)
        for i in range(repList['180']):
            myList.append(180)
        for i in range(repList['360']):
            myList.append(360)
        expFlag = 0
        for interval in myList:
            for i in range(interval):
                pdate = nextDay(pdate[0],pdate[1],pdate[2])
                if isNewer(pdate,edate):
                    expFlag = 1
                    break
            if expFlag==1:
                break
            dates.append(pdate)
    # if expFlag==1:
        # print('Overflow')
    if expFlag!=1:
        pdate = dates[-1]
        while not isNewer(pdate,edate):
            for i in range(myList[-1]):
                pdate = nextDay(pdate[0],pdate[1],pdate[2])
                if isNewer(pdate,edate):
                    expFlag = 1
                    break
            if expFlag==1:
                break
            dates.append(pdate)
    return dates

# dates = getRepDates(1,1,1)
# print(dates)