def encrypt(password):
	
	# Set the secret word for encryption.
	secretWord = "LetsEncryptIt"

	# Multiply the string secretWord until it is at least as long as the password
	while len(secretWord) < len(password):
		secretWord = secretWord + "LetsEncryptIt"

	# Initialize the encrypted newString and constuct it character by character
	# using the for loop spanning the password length.
	newString = ""
	for i in range(len(password)):
		compare = chr( ord(password[i]) ^ ord(secretWord[i]) )
		newString += compare

	# Return the now encrypted password in the form of the variable newString.
	return newString
