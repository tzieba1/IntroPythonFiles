array_list = [ "dog", "walked", "night" ]
replacement_list = [ "cat", "dragged", "day" ]

sentence = input( "Enter string: " )

loop = 0
while loop < len( array_list ):
    while array_list[ loop ] in sentence:
        position = sentence.find( array_list[ loop ] )
        word_length = len( array_list[ loop ] )

        sentence = sentence[ 0 : position ] + \
                   replacement_list[ loop ] + \
                   sentence[ position + word_length : ]
    
    loop += 1

print( "Your new sentence is: " )
print( sentence )
