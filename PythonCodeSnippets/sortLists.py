def sort( list ):
    p = 0
    while p < len( list ) - 1:

        swap = 0
        while swap < len( list ) - 1:
            if list[swap] > list[swap+1]:
                temp = list[swap]
                list[swap] = list[swap+1]
                list[swap+1] = temp

            swap += 1
        p += 1

# Main method

numbers = [2, 5, 9, 6, 1, 7, 8, 0, 3, 4]
minions = ["Droid", "Swamp Creature", "Cyborg", "Pirate", "Zombie", "Thing"]

print( numbers )
print( "" )
sort( numbers )
print( numbers )

print( "" )
print( minions )
sort( minions)
print( "" )
print( minions )
