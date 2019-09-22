
tests = [[50, 82, 47], [60, 94, 90], [87, 32, 83], [25, 63, 78], [95, 47, 62], [72, 71, 58]]

sum = 0

row = 0
while row < 6:

    col = 0
    while col < 3:
        sum += tests[ row ][ col ]
        
        col += 1

    row += 1

print( "The sum of all test scores is: ", sum )
print( "There are " + str( row * col ) + " test scores" )
print( "The average test score is: ", round( sum / ( row * col ), 1 ) )
