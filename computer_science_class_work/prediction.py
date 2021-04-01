
# Importing sys module to exit program due to invalid user iput
import sys


testcase = eval(input("Enter the number (1) if you'd like this program to initate a test case at the end, or (2) if not.\n"))


# Functions for running script with or without test case
def determine_generation_no_testcase(): 
 namevar = input("Hello, whats your name?:\n")
 print("Ok", namevar)
 age = eval(input("Enter the age you will be this year for ex: 36\n"))
 # Compute birth year by subtracting age from current year
 bdyearvar = (2021 - age)
 if   bdyearvar < 1901:
 	 # Raising exception due to invalid entry - terminate program and instruct to try again
 	 sys.exit("You entered the birthday of a deceased individual, pls try again and enter a living person's age")
 elif bdyearvar < 1910:
	 bdyearvar = "Interbellum Generation" 
 elif bdyearvar < 1923:
     bdyearvar = "Greatest Generation" 
 elif bdyearvar < 1946:
     bdyearvar = "Silent Generation" 
 elif bdyearvar < 1964:
     bdyearvar = "Baby Boomers"
 elif bdyearvar < 1996:
     bdyearvar = "Millennials"
 elif bdyearvar < 1980:
     bdyearvar = "Generation X"
 elif bdyearvar < 1996:
     bdyearvar = "Generation Y"
 elif bdyearvar < 2015:
     bdyearvar = "Generation Z"
 else: 
    # Raising exception due to un-born child's age - terminate program and instruct to try again
    sys.exit("You entered the birthday of an un-born individual, pls try again and enter a living person's age")
 
 # Displaying another computation of boolen to determine likely behavior
 carsvar = eval(input("From 1 - 10, how likely are you to buy another car in your lifetime?:\n"))
 fastcar = eval(input("From 1 -10, how much do you like fast cars?:\n"))
 likely_fastcar_var = carsvar > 5 and fastcar > 5   
 birthday=str(bdyearvar)
 print("Your Generation is guessed as: " +birthday)
 fastcar = str(likely_fastcar_var)
 print("Are you likely to buy a fast car in your lifetime true/or false: "+fastcar)
 # First input value should be a string
 print("Is name value a string?")
 isinstance(namevar, str)
 print("Is birthday year valid?")
 # Second input should be a valid age of a living person, if its someone outside the generation of Interbellum or Generation Z, its invalid
 determine_generation_no_testcase.bdyearvar > 1901 and bdyearvar < 2015
 print("Is car like from 1 - 10 a valid datatype?")
 isinstance(carsvar, int)



def determine_generation_add_testcase():
 namevar = input("Hello, whats your name?:\n")
 print("Ok", namevar)
 age = eval(input("Enter the age you will be this year for ex: 36\n"))
 # Compute birth year by subtracting age from current year
 bdyearvar = (2021 - age)
 if   bdyearvar < 1901:
      # Raising exception due to invalid entry - terminate program and instruct to try again 	 
      print("Testcase Failure, Birthday outside expected range:")
      # Input should be a valid age of a living person, if its someone outside the generation of Interbellum or Generation Z, its invalid
      bdyearvar > 1901 and bdyearvar < 2015
      sys.exit("You entered the birthday of a deceased individual, pls try again and enter a living person's age")
      # Raising exception due to invalid entry - terminate program and instruct to try again
      sys.exit("You entered the birthday of a deceased individual, pls try again and enter a living person's age")
 elif bdyearvar < 1910:
	 bdyearvar = "Interbellum Generation" 
 elif bdyearvar < 1923:
     bdyearvar = "Greatest Generation" 
 elif bdyearvar < 1946:
     bdyearvar = "Silent Generation" 
 elif bdyearvar < 1964:
     bdyearvar = "Baby Boomers"
 elif bdyearvar < 1996:
     bdyearvar = "Millennials"
 elif bdyearvar < 1980:
     bdyearvar = "Generation X"
 elif bdyearvar < 1996:
     bdyearvar = "Generation Y"
 elif bdyearvar < 2015:
     bdyearvar = "Generation Z"
 else: 
    print("Testcase Failure, Birthday outside expected range:")
    # Second input should be a valid age of a living person, if its someone outside the generation of Interbellum or Generation Z, its invalid
    bdyearvar > 1901 and bdyearvar < 2015
    # Raising exception due to un-born child's age - terminate program and instruct to try again
    sys.exit("You entered the birthday of an un-born individual, pls try again and enter a living person's age")
 
 # Displaying another computation of boolen to determine likely behavior
 carsvar = eval(input("From 1 - 10, how likely are you to buy another car in your lifetime?:\n"))
 fastcar = eval(input("From 1 -10, how much do you like fast cars?:\n"))
 likely_fastcar_var = carsvar > 5 and fastcar > 5   
 birthday=str(bdyearvar)
 print("Your Generation is guessed as: " + birthday)
 fastcar = str(likely_fastcar_var)
 print("Are you likely to buy a fast car in your lifetime true/or false: "+fastcar)




# Test Case
if testcase == 1:
     determine_generation_add_testcase()
else:
     determine_generation_no_testcase()
     
