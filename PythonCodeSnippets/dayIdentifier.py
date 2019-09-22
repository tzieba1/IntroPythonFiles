def someMaths( aNumber ):
    newNumber = aNumber // 1000
    newNumber = newNumber % 7
    return newNumber
    
def dayOfWeek( dayNumber ):
    if dayNumber == 0:
        dayString = "Sunday"
    elif dayNumber == 1:
        dayString = "Monday"
    elif dayNumber == 2:
        dayString = "Tuesday"
    elif dayNumber == 3:
        dayString = "Wednesday"
    elif dayNumber == 4:
        dayString = "Thursday"
    elif dayNumber == 5:
        dayString = "Friday"
    elif dayNumber == 6:
        dayString = "Saturday"
    return dayString

def daysFrom( oldDayNumber, howManyDays ):
    nextDay = ( oldDayNumber + howManyDays ) % 7
    dayString = dayOfWeek( nextDay )
    return dayString

studentNumber = int( input( "Please enter your student number: " ) )
calculatedNumber = someMaths( studentNumber )

print( calculatedNumber ) 

dayOne = dayOfWeek( calculatedNumber )
print( "The day of the week with that number is " + dayOne + "." )

dayTwo = daysFrom( calculatedNumber, 3 )
print( "3 days after it will be " + dayTwo + "." )

