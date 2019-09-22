validInput = False
while not validInput:
    province = input("please enter ON, PQ, or NFLD:")
    postalCode = input("Please enter the first 3 digits of your postal code: ")

    errorMessage = ""
    if province == "ON" or province == "PQ" or province == "NFLD":
        validProvince = True

    else:
        validProvince = False
        errorMessage = errorMessage + "Invalid Province\n"

    if province == "ON" and postalCode[0] in "KLMNP":
        validPostalCode = True
    elif province == "PQ" and postalCode[0] in "GHJ":
        validPostalCode = True
    elif province == "NFLD" and postalCode[0].lower() =="A":
        validPostalCode = True
    else:
        validPostalCode = False
        errorMessage = errorMessage + "Invalid Postal Code " +\
                       postalCode + " for province " + province

    validInput = validProvince and validPostalCode

    if not validInput:
        print(errorMessage)

print("Input accepted!")
