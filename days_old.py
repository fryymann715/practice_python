__author__ = 'Ian'
import webbrowser

def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1, 1

def dateIsBefore(y1, m1, d1, y2, m2, d2):
    if y1 < y2 or m1 < m2:
        return True
    else:
        return d1 < d2


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days = 0
    #assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days


def isLeapYear(year):
    if year % 4 == 0 or year % 400 == 0:
        return True
    else:
        return False

def test():
    print "*******************TEST BEGIN*******************"
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert dateIsBefore(2013, 12, 31, 2014, 1, 1) == True
    assert dateIsBefore(2013, 12, 31, 2013, 12, 30) == False
    assert daysBetweenDates(2013, 12, 31, 2014, 1, 1) == 1
    assert nextDay(2012, 7, 15) == (2012, 7, 16)
    assert nextDay(2012, 7, 31) == (2012, 8, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2012, 2, 28) == (2012, 2, 29)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert daysBetweenDates(2013, 7, 15, 2014, 7, 15)
    print "*******************TEST COMPLETE****************"

test()

webbrowser.open("https://mail.google.com/mail/u/0/?tab=wm#inbox/14e38528a5dbdd12")

print isLeapYear(2014)
print isLeapYear(2020)
print daysBetweenDates(1986, 7, 15, 2015, 6, 7)


