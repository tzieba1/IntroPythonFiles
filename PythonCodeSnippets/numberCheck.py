myString = ""
keepLooping = True

while myString.lower() != "q" and keepLooping != False :
    myString = input("A number: ")

    myNumber = ""

    isNegative = False
    isFloat = False
    isNumber = True
    firstNumberSeen = False
    decimalPointSeen = False
    loopCounter = 0

    while ( loopCounter < len( myString ) ) and isNumber :
        if myString[loopCounter].isdecimal():
            # positive integer found
            firstNumberSeen = True
            myNumber = myNumber + myString[loopCounter]
        elif myString[loopCounter] == "-":
            if not firstNumberSeen:
                isNegative = not( isNegative )
            else:
                isNumber = False
        elif myString[loopCounter] == "." or myString[loopCounter] == ",":
            if not decimalPointSeen:
                decimalPointSeen = True
                myNumber = myNumber + myString[loopCounter]
            else:
                isNumber = False
        else:
            isNumber = False

        loopCounter = loopCounter + 1

    if isNumber:
        if isNegative:
            myNumber = "-" + myNumber
            
        print( "Looks like the number", myNumber )

        if "." in myNumber:
            myNumber = float( myNumber )
        else:
            mynumber = int( myNumber )

        if myNumber > 6:
            keepLooping = False
    else:
        print( "Not a number" )
