# Serially assigning 3 numbers to variables a, b, c from user input.
a = float(input('Provide a number for variable "a": '))
b = float(input('Provide a number for variable "b": '))
c = float(input('Provide a number for variable "c": '))

#Calculating negative and positive roots and assigning these values corresponding
# variables.
neg_root = - b - ( ( b ** 2 -  4 * a * c ) ** ( 1 / 2 ) / 2 * a )
pos_root = - b + ( ( b ** 2 -  4 * a * c ) ** ( 1 / 2 ) / 2 * a )

# Compare 'neg_root' and 'pos_root' each with 0, i.e. Formula 1 and
# Formula 2 each compared to 0 with relation '>'. Next compare the resulting boolean
# values using 'and' operator to return another boolean. This boolean is converted
# to a string and ouputted in a concatenated statement.
print('It is ' + str( neg_root > 0 and pos_root > 0 ) + \
	' that roots are both positive.' )