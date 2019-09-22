
number = int(input("Give a number: "))
counter = 0
total_sum = 0

while counter < number:
    counter +=1
    total_sum = total_sum + number - counter

print("The value of the variable 'total_sum' is: " + str(total_sum)) 
