def getWeekday(today, later):
        if today <= 0  or today > 7:
                laterDay = "error: out of range"
        else:
		AfterLaterMod7 = (today - 1 + later)%7
		days = ["Sunday","Monday","Tuesday","Wednesday",\
				"Thursday","Friday","Saturday"]
		laterDay = days[afterLaterMod7]
        return laterDay
today = int(input("Please enter today's date (1-7)"))
later = int(input("PLease ender a number of days later"+\
					" to get the day of the week: "))
print(getWeekday(today, later))
