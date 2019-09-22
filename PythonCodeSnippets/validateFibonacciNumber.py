fibNum = 0
tempFibNum=1
num=int(input("give a number to check if its fibonacci: "))
while fibNum <= num:
    if num!=fibNum:
        oldFibNum = fibNum
        fibNum += tempFibNum
        tempFibNum = oldFibNum
    elif num == fibNum:
        print("Thats'a fibonacci!")
        break
    else:
        pass
    
    
    
