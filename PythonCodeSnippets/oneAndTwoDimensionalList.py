def oneDimensionalList():

	# Initialize loop that continues taking userInput and testing unless user inputs "quit"
	# in any letter-case comination.

        # Initialize non-'quit' user input.
	userInput = ""
	# Initialize an empty list of words.
	words = []
	lowerWords = []
	while userInput.lower() != "quit": 
		userInput = input("Input words or enter 'quit' to stop:\t")
		
		# Adds words in two lists, one with the first letter exclusively lowercase for sorting while taking input.
		if userInput.lower() != "quit":
			words.append(userInput)
			lowerWords.append(userInput[0].lower() + userInput[1:])
        
		# Sort the letters alphabetically with original input and with lowercase first-letters to be printed.
		else:
			words.sort()
			lowerWords.sort()
			
			# Loop through the alphabetical list of letters to be printed line by line.
			# Assume words are only capitalized for the first letter.
			for word in lowerWords:
				if ( word[0].upper() + word[1:] ) in words:
					print(word[0].upper() + word[1:])
				else:
					print(word)

	# Print statement stating that the module has ended when user quits.
	print("Module terminated. Good-bye.")
	return

def twoDimensionalList(n):
	
	userNum = n
	valid = False
	while valid == False:
		# Conditional statement for validating input. 
		# Consider negative numbers when using .isdigit().
		if str(userNum).isdigit() and (int(userNum) in range(3,10)):
			valid = True
			# Initialize a list to represent the table as a nxn matrix.
			multTable = []
			displayTable = ""
			# Looping through 'rows' of the matrix.
			for i in range(int(userNum) + 1):
                                
				# Initialize a row to be added to the matrix
				row = []
				displayTable += "\n"
				# Looping through 'columns' of the matrix.
				for j in range(int(userNum) + 1):
					row.append(i*j)
					displayTable += str(i*j) + "\t"
				#Adding a constructed row to the matrix.
				multTable.append(row)
				# Preparing rows of the matrix to be printed as a table.
				
                        # Print matrix as a list.
			print(multTable)
			print(displayTable)

		# Getting new input whenever invalid.
		else:
			userNum = input("That is not a valid integer, please try again:\t")	
	return

# MAIN

# Section 3.1: Starts oneDimentionalList() module.
oneDimensionalList()

# Section 3.2: Take user input (integer) to be passed into twoDimensionalList(n) module.
n = input("Input an integer between 3 and 9 (inclusive):\t")
twoDimensionalList(n)
