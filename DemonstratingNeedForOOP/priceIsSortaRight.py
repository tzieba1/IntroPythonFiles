# I, Tommy Zieba, student number 000797152, certify that all code submitted is my own
# work; that I have not copied it from any other source.  I also certify that I have
# not allowed my work to be copied by others.

import random 

def contestantsRow(host, contestant):
	# Giving names to the computer players and assigning a dictionary 
	# with key/value pairs of players/winnings whos values may be changed.
	# Winnings are represented with a list that has the total winnings and
	# a flag integer 0 (out of contestants row) or 1 (still in contestants row)
	
	p1 = "Becky"
	p2 = "Pedro"
	p3 = "Michael"
	p1Winnings = 0
	p2Winnings = 0
	p3Winnings = 0 
	cWinnings = 0
	
	print("The host " + host + " welcomes " + contestant + " to contestant's row. Joining them are ",
		p1 + ", " + p2 + ", and " + p3 +".\n")
	
	# Initialize a playerLedger to keep track of player winnings.
	playerLedger = { p1 : p1Winnings, p2 : p2Winnings, p3 : p3Winnings, contestant : cWinnings }
	

	loss = False
	trial = 1
	# Trials represent an instance where the human player does not have the best guess (up to 3)
	while trial < 4:
		
		
		
		
		
		# *=*=*=*=*=*=*=*FIRST TRIAL*=*=*=*=*=*=*=*
		if trial == 1:
			playersIn = { p1 : True, p2 : True, p3 : True, contestant : True }
			hiddenPrice = random.randint(50,1000)
			print("The host " + host + " shows the prize you will be bidding on.\n")
			
			# Takes the contestants guess and tests if it is an integer.
			cGuess = input(host + " says, '" + contestant + ", please guess the hidden (integer) price between"+\
				" 50 and 1000 dollars.':\t")
			while not(cGuess.isdigit()) or not(50 <= int(cGuess) <= 1000):
				cGuess = input(host + " says,'I'm sorry I couldn't make that out, a bid of"+\
					" at least $1 please.':\t")

			# Stores the player's guesses as a dictionary of key/value representing player/guess
			guess = { p1 : random.randint(50,1000), p2 : random.randint(50,1000),\
				p3 : random.randint(50,1000), contestant : cGuess }
			
			# Initialize a dictionary where guesses over 1000 represents overbidding and under 1000 represents the difference
			# between a good bid and the hiddenPrice.
			overPrice = { p1 : 1001, p2 : 1001, p3 : 1001, contestant : 1001 }
			
			# Checks that guess has no duplicates and re-generates new guesses if one exists
			# If there is a duplicate guess, the dictionary is updated with a
			# new computer guess which is checked repeatedly using the while loop.
			for i in guess:
				for j in guess:
					while (int(guess[i]) - int(guess[j]) == 0) and i != j:
						guess[i] = random.randint(50, 1000)

			# Announce the non-contestant pplayer guesses from the dictionary 'guess' holding 
			# validated guesses including the contestants.
			print("After " + host + " takes the other player-bids, the final results are:\n")
			for i in guess:
				print(i + " guessed:\t" + str(guess[i]) )
			
			print("\nThe value of the item the players are bidding on is:\t" + str(hiddenPrice) +"\n" )

			# Stores the players difference between their guess and hiddenPrice in a dictionary
			overPrice = { p1 : hiddenPrice - int(guess[p1]) , p2 : hiddenPrice - int(guess[p2]),\
			p3 : hiddenPrice - int(guess[p3]), contestant : hiddenPrice - int(guess[contestant]) }

			# Determines which guess is the best.
			# This is also the point where the nesting while loop makes sense to do because it
			# gives a easy way to reset the guesses without re-writing the code line for line
			# in the case that every guess is over. If all are overbidding, then every overPrice
			# value is > 1000 causing the while loop to reset which takes and validates 
			# other input and guesses.
			for i in overPrice:
				if int(overPrice[i]) < 0:
					overPrice[i] = 1000 - int(overPrice[i])
				else:
					pass
			bestGuess = min(int(overPrice[p1]), int(overPrice[p2]), int(overPrice[p3]),\
				int(overPrice[contestant]))
			
			# Checks if contestant has best guess and assigns $1000 to their winnings
			# and assigns $1000 to the winner in the playerLedger if computer player wins. 
			# Also assigns a roundWinner so that dictionaries may be re-used for the next trial.
			if bestGuess != int(overPrice[contestant]) and bestGuess <= 1000:
				for i in overPrice:
					if int(overPrice[i]) == bestGuess:
						playerLedger[i] = int(playerLedger[i]) + 1000
						roundWinner = i
					else:
						pass	
				trial += 1
				print(host + " says, 'It looks like the winner for this round of guessing is " + roundWinner +\
					". They will advance to the pricing game and will have $1000 added to their winnings.'\n")
			
			# Checks if everyone went over.
			elif bestGuess != int(overPrice[contestant]) and bestGuess > 1000:
				print( host + " turns to " + contestant + " and says, 'I'm sorry you didn't have better"+\
					" luck here today, but we're sending you home with the unofficial board game of The"+\
					" Price is (Sorta) Right.'\n")
				loss = True
				trial = 4
			else:
				playerLedger[contestant] = int(playerLedger[contestant]) + 1000
				roundWinner = contestant
				print(host + " congratulates " + contestant +"'s victory and gives him a"+\
					" prize of $1000. " + host + " announces that " + contestant + " moves"+\
					" on to the pricing game.\n")
				trial = 4
				
			# Changing playersIn and overPrice so that the dictionaries can be modified from the first
			#	trial's code.
			if not(loss):
				playersIn.pop(roundWinner)
				overPrice.pop(roundWinner)
			




		# *=*=*=*=*=*=*=*SECOND TRIAL*=*=*=*=*=*=*=*
		elif trial == 2:
			hiddenPrice = random.randint(50,1000)
			
			# Initialize the players for this round as a list and assigns the round players from the list
			playersInList = list(playersIn)
			roundP1 = playersInList[0]
			roundP2 = playersInList[1]
			roundP3 = playersInList[2]
			print("The host " + host + " shows the prize you will be bidding on.\n")
			
			# Takes the contestants guess and tests if it is an integer.
			cGuess = input(host + " says, '" + contestant + ", please guess the hidden (integer) price between"+\
				" 50 and 1000 dollars.':\t")
			while not(cGuess.isdigit()) or not(50 <= int(cGuess) <= 1000):
				cGuess = input(host + " says,'I'm sorry I couldn't make that out, a bid of"+\
					" at least $1 please.':\t")

			# Stores the player's guesses as a dictionary of key/value representing player/guess
			for i in playersInList:
				if i == contestant:
					guess[i] = cGuess
				else:
					guess[i] = random.randint(50, 1000)

			# Initialize a dictionary where guesses over 1000 represents overbidding and under 1000 represents the difference
			# between a good bid and the hiddenPrice.
			overPrice = { roundP1 : 1001, roundP2 : 1001, roundP3 : 1001 }
				
			# Checks that guess has no duplicates and re-generates new guesses if one exists
			# If there is a duplicate guess, the dictionary is updated with a
			# new computer guess which is checked repeatedly using the while loop.
			for i in guess:
				for j in guess:
					while (int(guess[i]) - int(guess[j]) == 0) and (i != j) and i != contestant:
						guess[i] = random.randint(50, 1000)
						guess[i]
			
			# Announce the non-contestant pplayer guesses from the dictionary 'guess' holding 
			# validated guesses including the contestants.
			print("After " + host + " takes the other player-bids, the final results are:\n")
			for i in playersIn:
				print(i + " guessed:\t" + str(guess[i]) )
			print("\nThe value of the item the players are bidding on is:\t" + str(hiddenPrice) +"\n" )

			# Stores the players difference between their guess and hiddenPrice in a dictionary.
			for i in playersInList:
				overPrice[i] = hiddenPrice - int(guess[i])
					
			# Determines which guess is the best.
			for i in playersIn:
				if int(overPrice[i]) < 0:
					overPrice[i] = 1000 - overPrice[i]
						
			bestGuess = min(int(overPrice[roundP1]), int(overPrice[roundP2]), int(overPrice[roundP3]))
			
			# Checks if contestant has best guess and assigns $1000 to their winnings
			# and assigns $1000 to the winner in the playerLedger if computer player wins. 
			# Also assigns a roundWinner so that dictionaries may be re-used for the next trial.
			if bestGuess != int(overPrice[contestant]) and bestGuess <= 1000:
				for i in overPrice:
					if (overPrice[i] == bestGuess) and (i != contestant):
						playerLedger[i] = int(playerLedger[i]) + 1000
						roundWinner = i
						trial = 3
					else:
						pass
				print(host + " says, 'It looks like the winner for this round of guessing is " + roundWinner +\
					". They will advance to the pricing game and will have $1000 added to their winnings.'\n" )
			
			# Checks if everyone went over.
			elif bestGuess != int(overPrice[contestant]) and bestGuess > 1000:
				print( host + " turns to " + contestant + " and says, 'I'm sorry you didn't have better"+\
					" luck here today, but we're sending you home with the unofficial board game of The"+\
					" Price is (Sorta) Right.'\n")
				loss = True
				trial = 4
			else:
				playerLedger[contestant] = int(playerLedger[contestant]) + 1000
				roundWinner = contestant
				print(host + " congratulates " + contestant +"'s victory and gives him a"+\
					" prize of $1000. " +host + " announces that " + contestant + " moves"+\
					" on to the pricing game.\n")
				trial = 4
		
			# Changing playersIn so that the dictionaries can be modified from the first
			#	trial's code.
			if not(loss):
				playersIn.pop(roundWinner)
				overPrice.pop(roundWinner)
		
		
		# *=*=*=*=*=*=*=*THIRD TRIAL*=*=*=*=*=*=*=*
		elif trial == 3:
			hiddenPrice = random.randint(50,1000)
			
			# Initialize the players for this round
			playersInList = list(playersIn)
			roundP1 = playersInList[0]
			roundP2 = playersInList[1]
				
			print("The host " + host + " shows the prize you will be bidding on.\n")
			
			# Takes the contestants guess and tests if it is an integer.
			cGuess = input(host + " says, '" + contestant + ", please guess the hidden (integer) price between"+\
				" 50 and 1000 dollars.':\t")
			while not(cGuess.isdigit()) or not(50 <= int(cGuess) <= 1000):
				cGuess = input(host + " says,'I'm sorry I couldn't make that out, a bid of"+\
					" at least $1 please.':\t")

			# Stores the player's guesses as a dictionary of key/value representing player/guess.
			for i in playersInList:
				if i == contestant:
					guess[i] = cGuess
				else:
					guess[i] = random.randint(50, 1000)
			
			# Initialize a dictionary where guesses over 1000 represents overbidding and under 1000 represents the difference
			# between a good bid and the hiddenPrice.
			overPrice = { roundP1 : 1001, roundP2 : 1001 }
				
			# Checks that guess has no duplicates and re-generates new guesses if one exists
			# If there is a duplicate guess, the dictionary is updated with a
			# new computer guess which is checked repeatedly using the while loop.
			for i in guess:
				for j in guess:
					while (int(guess[i]) - int(guess[j]) == 0) and (i != j) and i != contestant:
						guess[i] = random.randint(50, 1000)
			
			# Announce the non-contestant pplayer guesses from the dictionary 'guess' holding 
			# validated guesses including the contestants.
			print("After " + host + " takes the other player-bids, the final results are:\n")
			for i in playersIn:
				print(i + " guessed:\t" + str(guess[i]) )
			print("\nThe value of the item the players are bidding on is:\t" + str(hiddenPrice) +"\n" )

			# Stores the players difference between their guess and hiddenPrice in a dictionary.
			for i in playersInList:
				overPrice[i] = hiddenPrice - int(guess[i])
					
			# Determines which guess is the best.
			for i in playersIn:
				if int(overPrice[i]) < 0:
					overPrice[i] = 1000 - overPrice[i]
					
			bestGuess = min(int(overPrice[roundP1]), int(overPrice[roundP2]))
			
			# Checks if contestant has best guess and assigns $1000 to their winnings
			# and assigns $1000 to the winner in the playerLedger if computer player wins. 
			# Also assigns a roundWinner so that dictionaries may be re-used for the next trial.
			if bestGuess != int(overPrice[contestant]) or bestGuess > 1000:
				print( host + " turns to " + contestant + " and says, 'I'm sorry you didn't have better"+\
					" luck here today, but we're sending you home with the unofficial board game of The"+\
					" Price is (Sorta) Right.'\n")
				loss = True
				trial = 4
			else:
				playerLedger[contestant] = int(playerLedger[contestant]) + 1000
				roundWinner = contestant
				print(host + " congratulates " + contestant +"'s victory and gives him a"+\
					" prize of $1000. " + host + " announces that " + contestant + " moves"+\
					" on to the pricing game.\n")
				trial = 4
		else:
			pass
	return [playerLedger, loss]

def pricingGame(host, contestant, playerLedger):
	# Initialize number of strikes and a random 5 digit integer as a string.
	strikes = 0
	loss = False
	carPrice = str(random.randint(10000,30000))
	
	# Introducing the pricing game.
	print( host + " says, 'Today we're playing Three Strikes.'\n")
	
	# Assigning the digits of carPrice in a dictionary such that keys can be randomly
	# selected to produce values and updated to remove key/values properly placed
	# in the carPrice digits.
	bag = {5 : "X"}
	for i in range(0,5):
		bag[i] = carPrice[i]
	
	# Initialize dictionary for balls taken out and a counter for number of balls 
	# removed successfully.
	ballsOut = []
	ballsCorrect = 0
	

		
	# Loop for continuing play while strikes are not all used.
	while strikes != 3:
		
		input(host + " says, 'Go ahead " + contestant + ". Pick a ball from the bag!':\t(press enter to pick a ball)")
		
		# Select a ball randomly and while it is not in the list of ballsOut, get another ball until valid.
		ball = bag[random.randint(0,5)]
		while ball in ballsOut:
			ball = bag[random.randint(0,5)]
		print(host + " says, '" + contestant + " you've picked " + str(ball) + ".'")
		
		#Handles the case where the ball is a strike.
		if ball == "X" and strikes != 2:
			strikes += 1
			print( host + " says, 'Oh no, a strike. That's ok, you've used " + str(strikes) + " strikes.'\n")
		# Handles the case where the ball is the third strike
		elif ball == "X" and strikes == 2:
			print(host + " says, 'I'm sorry, but thats 3 strikes which means you've lost.'\n")
			strikes += 1
			loss = True
		
		# Handles the case where the ball is not a strike.
		else:
			
			# Contestant choosing a position from 1 to 5 and verifying it is a valid integer ( assume integer input ).
			position = int(input( host + " says, 'Which position, 1 to 5, does this number belong in?':\t")) - 1
			if not(int(position) in range(0,6)):
				position = int(input( host + " says, 'I couldn't make that out, please pick a number"+\
					" from 1-5 nice and clearly for us.':\t")) - 1
			
			# Checks if contestant's choice of digit is correct using the carPrice and position.
			# Removes the ball from the bag if digit is correctly chosen.
			# Updates ballsOut to account for the one coming out of the bag
			elif carPrice[position] == ball:
				print( host + " says, 'That's correct! Let's light up the " + str(ball) + ".'\n")
				ballsOut.append(ball)
			else:
				strikes += 1
				print( host + " says, 'Ohhhh, I'm sorry, that's incorrect, that one goes"+\
					" back in the bag. That also counts as a strike. You now have " + str(strikes) +".' \n")
				
		# Checks if the player has guessed all the digits without having three strikes to win.
		# If the player wins, the while loop is exited by breaking.
		if strikes != 3 and len(ballsOut) == 5:
			print("Bells ring, lights flash, and " + host + " turns and exclaims, 'You've"+\
				" done it! That car is all yours!'\n")
			print(host + " exclaims, 'You correctly guessed the retail price of $" + carPrice + " !\n")
			break

	# Updates the playerLedger and returns its updated values.
	playerLedger[contestant] += int(carPrice)
	return [playerLedger, loss]

def wheelSpin():
	# Assigns a dictionary of the possible wheelValues with integers as keys (for random selection).
	wheelValue = { 0:5, 1:10, 2:15, 3:20, 4:25, 5:30, 6:35,\
		7:40, 8:45, 9:50, 10:55, 11:60, 12:65, 13:70, 14:75,\
		15:80, 16:85, 17:90, 18:95, 19:100 }
	
	# Returns a random wheelSpin from wheelValues 	
	return wheelValue[random.randint(0,19)]

def showcaseShowdown(host, contestant, playerLedger):
	
	print("It's now time for the showcase showdown! Let's see the remaining players spinthe big wheel.")
	# Check which non-contestant players won contestants row and assign them to
	# a dictionary representing players only in showcase showdown with values all boolean True.
	# Also assigns random winnings to non-contestant players from the pricing game.
	showcasePlayers= []
	playerCount = 0
	
	for player in playerLedger:
		if playerLedger[player] == 1000 and player != contestant:
			showcasePlayers.append(player)
			playerLedger[player] =  int(playerLedger[player]) + random.randint(0,30000)
			playerCount += 1
		elif player == contestant:
			showcasePlayers.append(contestant)
			playerCount += 1
		else:
			pass

	# If one or none of the non-contestants win contestants row, add new players
	# to the showcasePlayers dictionary.
	playerPool = ["Paul" , "Irene" ]
	if playerCount == 1:
		for player in playerPool:
			showcasePlayers.append(player)
			playerLedger[player] = 1000 + random.randint(0,30000)
	elif playerCount == 2:
		showcasePlayers.append(playerPool[0])
		playerLedger[playerPool[0]] = 1000 + random.randint(0,30000)
	else:
		pass

	# Initializes a dictionary for player cumulative spin values.
	spinValues = { showcasePlayers[0] : 0, showcasePlayers[1] : 0, showcasePlayers[2] : 0 }

	
	
	# Take turns spinning the wheel following the list: 'showcasePlayers'
	player = 0
	while player <= 2: 
		
		
		# 				************** First players turn to spin *****************
		if player == 0:
			spinPlayer = showcasePlayers[player]
			
			# Starts a loop which has sentinal value stopSpin asking the user to continue spinning
			# or assigning 'yes' or 'no' for non-contestants
			stopSpin = 'no'
			spinsUsed = 0
			eliminated = []
			while stopSpin == "no" and spinsUsed < 2:
				input( host + " says, 'Go ahead and spin the wheel " + spinPlayer +\
					".':\t (press enter to continue)")
				spin = wheelSpin()
				spinsUsed += 1
				print( host + " announces, '" + spinPlayer + " has spun " + str(spin) + "!'\n")
				spinValues[spinPlayer] += spin

				# Event that a dollar is reached
				if (spin == 100 and spinValues[spinPlayer] == 0) ^ (spinValues[spinPlayer] == 100):
					playerLedger[spinPlayer] += 1000
					stopSpin = 'yes'
					print( host + " says, 'Congratulations " + spinPlayer + ", you've won $1000!'\n")
				
				# Event that the spinPlayer goes over a dollar.
				elif spinValues[spinPlayer] > 100:
					stopSpin = 'yes'
					eliminated.append(spinPlayer)
					print(host + " says, 'I'm sorry " + spinPlayer + " but you've been eliminated.'\n")
				
				# Event that the spinPlayer doesn't reach a dollar.
				else:

					# Validates if it is the contestant to either take input stopSpin xor 
					# stop spinning for non-contestants whenever their spinValue <= 70
					if spinPlayer == contestant and spinsUsed < 2:
						stopSpin = input(host + " says, '" + contestant + ", you have " + str(spinValues[spinPlayer]) +\
						" cents,  which is less than $1.00, would you like to stop spinning, 'yes' or 'no'?'\n")
						if stopSpin == 'no' and spinsUsed == 1:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
						else:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							spinsUsed = 2
					elif spinPlayer != contestant and spinsUsed < 2:
						if spinValues[spinPlayer] <= 70 and spinsUsed == 1:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
							stopSpin = 'no'
						else:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							stopSpin = 'yes'
							spinsUsed = 2
					else:
						print(host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
			player += 1
		
		
		
		#                  **********Second player takes turns spinning wheel*********
		elif player == 1:
			spinPlayer = showcasePlayers[player]

			# Starts a loop which has sentinal value stopSpin asking the user to continue spinning
			# or assigning 'yes' or 'no' for non-contestants unless players have spun twice
			stopSpin = 'no'
			spinsUsed = 0
			while stopSpin == "no" and spinsUsed < 2:
				input( host + " says, 'Go ahead and spin the wheel " + spinPlayer +\
					".':\t (press enter to continue)")
				spin = wheelSpin()
				spinsUsed += 1
				print( host + " announces, '" + spinPlayer + " has spun " + str(spin) + "!'\n")
				spinValues[spinPlayer] += spin

				# Event that a dollar is reached
				if (spin == 100 and spinValues[spinPlayer] == 0) ^ spinValues[spinPlayer] == 100:
					playerLedger[spinPlayer] += 1000
					stopSpin = 'yes'
					print( host + " says, 'Congratulations " + spinPlayer + ", you've won $1000!'\n")

				# Event that the spinPlayer goes over a dollar.
				elif spinValues[spinPlayer] > 100:
					stopSpin = 'yes'
					eliminated.append(spinPlayer)
					print(host + " says, 'I'm sorry " + spinPlayer + " but you've been eliminated.'\n")	

				# Event that second spinPlayer scored less than first
				else:
					# Validates if it is the contestant to either take input stopSpin xor 
					# stop spinning for non-contestants whenever their spinValue <= 70
					if spinPlayer == contestant and spinsUsed < 2:
						stopSpin = input(host + " says, '" + contestant + ", you have " + str(spinValues[spinPlayer]) +\
							" cents, which is less than $1.00, would you like to stop spinning, 'yes' or 'no'?'\n")
						if stopSpin == 'no' and spinsUsed == 1:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
						else:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							spinsUsed = 2
					elif spinPlayer != contestant and spinsUsed < 2:
						if spinValues[spinPlayer] <= 70 and spinsUsed == 1:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
							stopSpin = 'no'
						else:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							stopSpin = 'yes'
							spinsUsed = 2
					else:
						print(host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
			player += 1
		
		
		
		
		#             *************** Final player spins the wheel. ****************
		elif player == 2:
			spinPlayer = showcasePlayers[player]

			# Starts a loop which has sentinal value stopSpin asking the user to continue spinning
			# or assigning 'yes' or 'no' for non-contestants
			stopSpin = 'no'
			spinsUsed = 0
			while stopSpin == "no" and stopSpin != 'yes' and spinsUsed < 2:
				input( host + " says, 'Go ahead and spin the wheel " + spinPlayer +\
					".':\t (press enter to continue)")
				spin = wheelSpin()
				spinsUsed += 1
				print( host + " announces, '" + spinPlayer + " has spun " + str(spin) + "!'\n")
				spinValues[spinPlayer] += spin

				# Proceeds by spinning appropriate number of times based on eliminated players
				if len(eliminated) == 2:
					print(host + " says, 'Since all other players are eliminated, " + spinPlayer +\
						" only gets one spin.'\n")
					stopSpin = "yes"
					spinsUsed = 2
				
				# Event that a dollar is reached
				elif (spin == 100 and spinValues[spinPlayer] == 0) ^ spinValues[spinPlayer] == 100:
					playerLedger[spinPlayer] += 1000
					stopSpin = 'yes'
					print( host + " says, 'Congratulations " + spinPlayer + ", you've won $1000!'\n")

				# Event that the spinPlayer goes over a dollar.
				elif spinValues[spinPlayer] > 100:
					stopSpin = 'yes'
					eliminated.append(spinPlayer)
					print(host + " says, 'I'm sorry " + spinPlayer + " but you've been eliminated.'\n")
				else:
					# Validates if it is the contestant to either accept input stopSpin xor 
					# stop spinning for non-contestants whenever their spinValue <= 70
					if spinPlayer == contestant and spinsUsed < 2:
						stopSpin = input(host + " says, '" + contestant + ", you have " + str(spinValues[spinPlayer]) +\
							" cents, which is less than $1.00, would you like to stop spinning, 'yes' or 'no'?'\n")
						if stopSpin == 'no' and spinsUsed == 1:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
						else:
							print( host + " says,'" + contestant + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							spinsUsed = 2
					elif spinPlayer != contestant and spinsUsed < 2:
						if spinValues[spinPlayer] <= 70 and spinsUsed == 1:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + \
								" and they've decided to keep spinning.'\n")
							stopSpin = 'no'
						else:
							print( host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
							stopSpin = 'yes'
							spinsUsed = 2
					else:
						print(host + " says,'" + spinPlayer + "'s total is " + str(spinValues[spinPlayer]) + ".'\n")
				
			# Check spinValues to determine who is eliminated and find the maxSpin value.
			maxDict = {}
			for i in spinValues:
				if spinValues[i] <= 100:
					maxDict[i] = spinValues[i]
					
			maxSpin = max( list( maxDict.values() ) )
			for i in spinValues:
				if spinValues[i] == maxSpin:
					maxSpinPlayer = i
			
			for j in spinValues:
				
				# Event that the other players spins are equal to maxSpin
				if maxSpinPlayer != j and spinValues[j] == maxSpin :
						print( host + " says, '" + j + " has tied with " + maxSpinPlayer +\
							" and so they both advance.'\n")
				# Event that the other players spins are less than maxSpin.
				elif maxSpinPlayer != j and spinValues[j] < maxSpin:
					print(host + " says, 'I'm sorry " + j + ", but "+\
						maxSpinPlayer + " scored more than you and you have been eliminated.'\n")
					eliminated.append(j)
				else:
					pass
					
					
			player += 1

	
	
	
	#                          *********** Bonus spins ************
	
	# Initializes an empty dictionary which will hold the bonusSpin values of each player.
	tieSpins = { showcasePlayers[0] : spinValues[showcasePlayers[0]],\
		showcasePlayers[1] : spinValues[showcasePlayers[1]], showcasePlayers[2] : spinValues[showcasePlayers[2]] }
	
	# Bonus spins awarded whenever at least one player spun $1.
	if spinValues[showcasePlayers[0]] == 100 or spinValues[showcasePlayers[1]] == 100 or spinValues[showcasePlayers[2]] == 100:
		print( host + " says, 'Since a player has spun $1.00, everyone gets a bonus spin!'\n")

		# Looping through the players' bonus spins.
		for i in showcasePlayers:
			if not(i in eliminated):
				spin = wheelSpin()
				tieSpins[i] = spin
	
				# Tests conditions for the spin of each layer "i" in the for loop to check/assign bonus prize money. 
				if spin == 100:
					print( host + " says, '" + i + " you've spun $1.00, which means you've won $25,000!'\n")
					playerLedger[i] = int(playerLedger[i]) + 25000
				elif spin == 5 or spin == 15:
					print( host + " says, '" + i + " you've spun " + str(spin) +\
						" cents, which means you've won $10,000!'\n")
					playerLedger[i] = int(playerLedger[i]) + 10000
				else:
					print( i + " has spun a value of " + str(spin))
		bonus = True
	else:
		print( host + " announces, 'There won't be any bonus spins today because no one has spun $1.'\n")
		bonus = False

	# Continues spinning to end ties between players by looping through possible ties.
	# Initialize variable to flag whether a tie exists.
	tie = True
	while tie == True:
		numTies = 0
		for i in showcasePlayers:
			for j in showcasePlayers:
					if (i not in eliminated) and (j not in eliminated):
						# Two-way ties between spinValues whenever no bonus spins awarded,
						if i != j and  tieSpins[i] == tieSpins[j] and bonus == False :
							numTies += 1
							print( host + " says, 'It looks like " + i + " and " + j + " must spin for a tie-breaker.'\n")
							tieSpins[j] = wheelSpin()
							tieSpins[i] = wheelSpin()
							print( host + "says,'" + i + " and " + j + " have spun " + str(tieSpins[i]) + " and " +\
								str(tieSpins[j]) + " respectively.'\n")
	
							# 'bonus' flag must be switched to reach the next elif in the following iteration of while loop.
							# i.e. the next elif is used for a tiebreaker after the first round of spins xor bonus spins
							bonus = True
							
						# Checks 'tieSpins' for two-way ties since it holds possible bonus spins or tie breaking spins otherwise.
						elif i != j and tieSpins[i] == tieSpins[j] and bonus == True:
							numTies += 1 
							print( host + " says, 'It looks like " + i + " and " + j + " must spin for a tie-breaker.'\n")
							tieSpins[j] = wheelSpin()
							tieSpins[i] = wheelSpin()
							print( host + "says,'" +  + " and " + j + " have spun " + str(tieSpins[i]) + " and " +\
								str(tieSpins[j]) + " respectively.'\n")
						
						# Three-way ties between spinValues whenever no bonus spins awarded
	
						elif spinValues[showcasePlayers[0]] == spinValues[showcasePlayers[1]] == spinValues[showcasePlayers[2]] and bonus == False :
							numTies += 1
							print( host + " announces, 'There won't be any bonus spins today because no one has spun $1.'\n")
							print( host + " says, 'It looks like a three-way tie, so all must spin for a tie-breaker.'\n")
							tieSpins[showcasePlayers[0]] = wheelSpin()
							tieSpins[showcasePlayers[1]] = wheelSpin()
							tieSpins[showcasePlayers[2]] = wheelSpin()
							print( host + "says,'" + showcasePlayers[0] + ", " + showcasePlayers[1] + " and " + showcasePlayers[2] +\
								" have spun " + str(tieSpins[showcasePlayers[0]]) + " , " + str(tieSpins[showcasePlayers[1]]) +\
								" and " + str(tieSpins[showcasePlayers[2]]) + " respectively.'\n")
	
							# 'bonus' flag must be switched to reach the next elif in the following iteration of while loop.
							# i.e. the next elif is used for a tiebreaker after the first round of spins xor bonus spins
							bonus = True
	
						# Three-way ties held in tieSpins after bonus spins or without bonus spins.
						elif tieSpins[showcasePlayers[0]] == tieSpins[showcasePlayers[1]] == tieSpins[showcasePlayers[2]] and bonus == True:
							numTies += 1
							print( host + " says, 'It looks like a three-way tie, so all must spin for a tie-breaker.'\n")
							tieSpins[showcasePlayers[0]] = wheelSpin()
							tieSpins[showcasePlayers[1]] = wheelSpin()
							tieSpins[showcasePlayers[2]] = wheelSpin()
							print( host + "says,'" + showcasePlayers[0] + ", " + showcasePlayers[1] + " and " + showcasePlayers[2] +\
								" have spun " + str(tieSpins[showcasePlayers[0]]) + " , " + str(tieSpins[showcasePlayers[1]]) +\
								" and " + str(tieSpins[showcasePlayers[2]]) + " respectively.'\n")
								
						# Checks if the number of ties counted is 0 after checking for ties and taking extra spins.
						# Changes the flag for the loop for eliminating ties and reaching a winner
						elif numTies == 0:
							tie = False
						
						else:
							pass

	# When there are no ties left, the tieSpins are checked because it holds the final result of
	# spins associated to players in a dictionary that were updated until all were different.
	# The winner is assigned and awarded.
	for i in eliminated:
		tieSpins.pop(i)
		tieSpins
		
	winSpin = max( list(tieSpins.values()) )
	for i in tieSpins:
		if tieSpins[i] == winSpin:
			winner = i
		else:
			pass

	# Finally, the module returns the winner of the game.		
	return [winner, playerLedger]


# MAIN ROUTINE

print("The Price is Sorta Right - 000797152\n")

host = "Bob Meower"

# User input of contestant name and initializing winnings.
contestant = input(host + " says, 'Tell us your name.' (letters only):\t")


# Verifying that the user inputted a valid name and prompt for another input.
count = 0
i = 0
while i < len(contestant):
	letter = contestant[i].lower()
	if letter.isalpha():
		count += 1
	else:
		contestant = input("Your name may only be alphabetical. Please try again:\t")
		count = 0
		i = -1
	i += 1
contestant = contestant[0].upper() + contestant[1:count]	


print(host + " announces, '" + contestant + "! Come on down! You're the next contestant on " +\
	"the Price is (Sorta) Right!'\n")

# Running module contestantsRow and return the playerLedger and assign to the same variable name.
contRowResults = contestantsRow(host, contestant)
playerLedger = contRowResults[0]

# Checks if contestants row was lost to continue the game or not.
if not(contRowResults[1]):
	
	# Running module pricingGame and returning the updated playerLedger.
	threeStrikesResults = pricingGame(host, contestant, playerLedger)
	playerLedger = threeStrikesResults[0]
	
	# Checks if pricingGame was lost to continue game or not.
	if not(threeStrikesResults[1]):
		
		# Running module showcaseShowdown and returning the winner and playerLedger in a list of two objects.
		showcaseResult = showcaseShowdown(host, contestant, playerLedger)
		winner = showcaseResult[0]
		playerLedger = showcaseResult[1]
		print(host + " congratulates " + winner + " for winning $" + str(playerLedger[winner]) +\
			" in cash and prizes!\n")
		print(host + " turns to face the audience saying, 'Help control the animal population,"+\
			" have your pet spayed or neutered!' and waves goodbye to everyone.\n")
		
		
	
