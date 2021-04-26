# Python Assignment Week 2
# By: Sulayman Touray


# Pay per hour is 40 dollars
hourlypay = 40.00

# Obtaining hours worked
prompt = "How many hours did you work this week? \n"
hoursworked = int(input(prompt))

# Pay total calculated
payearned = (hoursworked * hourlypay)



# Sales made are 10.00 dollars per sale, commission is 50% of total sales
prompt = "How many sales did you make this week? \n"
sales = int(input(prompt)) # user will input sales made


salesmade = (sales * 10.00) # calculate dollar sum of sales
# Compute commission 50% for final commission pay
commission = (0.5 * salesmade)



print ("Break Down:")
print ("Amount of sales", salesmade)
print ("Commission 50% of sales", commission)
print ("Weekly Pay", payearned)

# Results for final paycheck
print ("Final Paycheck:")
print ("Weekly pay + commision", payearned + commission )