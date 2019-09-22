# Uppercase ONLY the first word of a sentence.

# ASSUME Words are separated by " " and there are at least 2 words in
#        every sentence.

myString = input("A sentence of 2 or more words: ")

loopCounter = 0
keepLooping = True

while keepLooping:
    if myString[ loopCounter ].isspace():
        spacePosition = loopCounter
        keepLooping = False

    loopCounter += 1 # means loopCounter = loopCounter + 1


firstWord = myString[ 0 : spacePosition ]
firstWord = firstWord.upper()
restOfSentence = myString[ spacePosition : len(myString) ]

print( "Your new sentence is:", firstWord + restOfSentence )
