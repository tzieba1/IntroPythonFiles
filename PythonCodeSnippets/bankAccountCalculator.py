
# GET amount of money in bank
amount_in_bank = input("How much money is in the bank? $")
# GET amount of income
amount_of_income = input("How much income is expected? $")
# GET amount of expenses
amount_of_expenses = input("How much money is going to be spent on expenses? $")
# CALCULATE money in bank + income - expenses
# SET amount available to result of previous calculation
amount_available = int(amount_in_bank)+int(amount_of_income) - int(amount_of_expenses)
# DISPLAY amount available
message = "You will have $"+str( amount_available )+" left at the end of the month."
print ( message )