myPassword = input( "Please enter a password: " )

validLength = False
validUpper = False
validLower = False
validNumber = False

while not (validLength and validUpper and validLower and validNumber):

    length = len( myPassword )
    
    if length >= 8:
        validLength = True

    loop = 0
    while loop < length:
        if myPassword[loop].isupper():
            validUpper = True

        if myPassword[loop].islower():
            validLower = True

        if myPassword[loop].isdecimal():
            validNumber = True

        loop += 1

    if not (validLength and validUpper and validLower and validNumber):
        print( "Your password is invalid, try again" )
        myPassword = input( "Please enter a password: " )

print( "Your password is:", myPassword )




