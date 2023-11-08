import datetime

DAYS = ('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
MONTHS = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')

print('Calendar maker:')

while True:
    print('Enter the year of the calendar')
    response = input('> ')

    if response.isdecimal() and int(response) > 0:
        year = int(response)
        break

    print('Please enter a numeric year like 2023')

while True:
    print('Enter the month of the year, 1-12')
    response = input('> ')

    if not response.isdecimal():
        print('Please enter a numeric month, like 3 for March')
        continue

    month = int(response)
    if 1 <= month <= 12:
        break

    print('Please enter a number between 1-12')

def getCalendarFor(year, month):
    calText = ''
    
    calText += (' ' * 34) + MONTHS[month - 1] + ' ' + str(year) + '\n'
    calText += '...Sunday.....Monday....Tuesday...Wednesday... Thursday....Friday....Saturday..\n'
    weekSeparator = ('+----------' * 7) + '+\n'
    blankRow = ('| ' * 7) + '|\n'
    
    currentDate = datetime.date(year, month, 1)

    # Subtract days from currentDate until it's Sunday
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(days=1)

    while True:
        calText += weekSeparator
        dayNumberRow = ''

        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += '|' + dayNumberLabel + (' ' * 8)
            currentDate += datetime.timedelta(days=1)

        dayNumberRow += '|\n'
        calText += dayNumberRow

        for i in range(3):
            calText += blankRow

        if currentDate.month != month:
            break

    calText += weekSeparator
    return calText

calText = getCalendarFor(year, month)
print(calText)


#calendarFilename = 'calendar_{}_{}.txt'.format(year, month)
#with open(calendarFilename, 'w') as fileobj:
 #   fileobj.write(calText)

#print('Saved to ' + calendarFilename)