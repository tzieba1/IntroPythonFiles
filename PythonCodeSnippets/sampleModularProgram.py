#MODULE DEFINITION
def module(parameter1, parameter2, parameter3):
    variable1 = parameter1*parameter2
    variable2 = variable1//parameter3
    return variable2

#MAIN ROUTINE
userDecimal1 = float(input("Enter a decimal number to be multiplied."))
userDecimal2 = float(input("Enter another decimal number to be multiplied."))
userInt = input(("Enter a decimal for floor division"))

resultOfModule = module(userDecimal1, userDecimal2, userInt)
print(resultOfMOdule)

