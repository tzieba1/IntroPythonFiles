def imperialToCentimeters( feet, inches ):
        # CALCULATE total inches = feet * 12 + inches
	totalInches = feet * 12 + inches
        # CALCULATE total centimeters = total inches * 2.54
	totalCentimeters = totalInches * 2.54
	return totalCentimeters

# GET User's height in feet and inches
prompt = "How many feet tall are you? "
heightInFeet = int( input( prompt ) )

prompt = "How many inches taller than " \
         + str( heightInFeet ) + " feet are you? "
heightInInches = int( input( prompt ) )

# CALCULATE total centimeters from feet and inches
heightInCentimeters = \
   imperialToCentimeters( heightInFeet, heightInInches )

# SET User's height in meters to total centimeters // 100
heightInMeters = int( heightInCentimeters // 100 )

# SET User's height centimeters to total centimeters % 100
heightInCentimeters = heightInCentimeters % 100

# DISPLAY User's height in meters and centimeters
message = "Your metric height is " + str( heightInMeters ) \
          + " meter(s) and " + str(round( heightInCentimeters, 2 ) ) \
          + " centimeters."
print( message )
