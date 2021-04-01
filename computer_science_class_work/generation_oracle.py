
# Written by: Sulayman Touray
# Introduction to Problem Solving & Algorithm Design
#_____________________________________________________
#-oooooooo/-      .+ooooooooo:  +ooo+        oooo/
#+MMMMMMMMMMm+   -NMMMMMMMMMMs  +MMMM:      /MMMM/
#+MMMNyyydMMMMy  /MMMMyyyyyyy/   mMMMd      mMMMd
#+MMMm    :MMMM. /MMMN           /MMMM/    /MMMM:
#+MMMm    .MMMM- /MMMN            dMMMm    mMMMh
#+MMMm    .MMMM- /MMMMyyyy+       :MMMM/  +MMMM-
#+MMMm    .MMMM- /MMMMMMMMy        hMMMm  NMMMy
#+MMMm    .MMMM- /MMMMoooo:        -MMMM+oMMMM-
#+MMMm    .MMMM- /MMMN              yMMMmNMMMy
#+MMMm    +MMMM. /MMMN              .MMMMMMMM.
#+MMMMdddNMMMMo  /MMMMddddddd+       sMMMMMMs
#+MMMMMMMMMNh:   .mMMMMMMMMMMs        yMMMMs
#.///////:-        -/////////-         .::.


# Importing sys module to exit program due to invalid user input / failed test case
import sys

# Run script with or without test case
testcase = eval(input("Enter number (1) for script w/testcase, (2) for script no test case.\n"))


# To facilitate running the script with or without testing, 2 functions have been created to consolidate code
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
 elif bdyearvar < 2020:
     bdyearvar = "Generation Z or younger (infant)"
 else: 
    # Raising exception due to un-born child's age - terminate program and instruct user to try again
    sys.exit("You entered the birthday of an un-born individual, pls try again and enter a living person's age")
 
 # Displaying another computation of boolen to determine likely behavior in purchasing a "fast" car
 carsvar = eval(input("From 1 - 10, how likely are you to buy another car in your lifetime?:\n"))
 fastcar = eval(input("From 1 -10, how much do you like fast cars?:\n"))
 likely_fastcar_var = carsvar > 5 and fastcar > 5   
 birthday=str(bdyearvar)
 print("Your Generation is guessed as: " +birthday)
 fastcar = str(likely_fastcar_var)
 print("Are you likely to buy a fast car in your lifetime true/or false: "+fastcar)




# This function has test cases embedded to examine user values 
def determine_generation_add_testcase():
 namevar = input("Hello, whats your name?:\n")
 print("Ok", namevar)
 age = eval(input("Enter the age you will be this year for ex: 36\n"))

 # Compute birth year by subtracting age from current year
 bdyearvar = (2021 - age)
 if   bdyearvar < 1901:
      print("Initiating test cases:")  # Inititate test cases immediately to capture known exception
      print("Is name value a string?")
      print(isinstance(namevar, str))
      print("Is birthday year valid?")
      print(bdyearvar > 1901 and bdyearvar < 2020) # Second input should be a valid age of a living person

      # Raising exception due to invalid entry - terminate program and instruct to try again
      sys.exit("Failed test case detected, you entered the birthday of a deceased individual, pls try again and enter a living person's age")
 elif bdyearvar < 1910:
	 bdvar = "Interbellum Generation" 
 elif bdyearvar < 1923:
     bdvar = "Greatest Generation" 
 elif bdyearvar < 1946:
     bdvar = "Silent Generation" 
 elif bdyearvar < 1964:
     bdvar = "Baby Boomers"
 elif bdyearvar < 1996:
     bdvar = "Millennials"
 elif bdyearvar < 1980:
     bdvar = "Generation X"
 elif bdyearvar < 1996:
     bdvar = "Generation Y"
 elif bdyearvar < 2020:
     bdvar = "Generation Z or younger (infant)"
 else: 
     print("Initiating test cases:")  # Inititate test cases immediately to capture known exception
     print("Is name value a string?")
     print(isinstance(namevar, str))
     print("Is birthday year valid?")
     print(bdyearvar > 1901 and bdyearvar < 2020) # Second input should be a valid age of a living person

     # Second input should be a valid age of a living person, if its someone outside the generation of Interbellum or Generation Z, its invalid
     bdyearvar > 1901 and bdyearvar < 2020
     # Raising exception due to un-born child's age - terminate program and instruct to try again
     sys.exit("Failed testcase detected, you entered the birthday of an un-born individual, pls try again and enter a living person's age")
 
 # Displaying another computation of boolen to determine likely behavior to purchase a "fast" car
 carsvar = eval(input("From 1 - 10, how likely are you to buy another car in your lifetime?:\n"))
 fastcar = eval(input("From 1 -10, how much do you like fast cars?:\n"))
 likely_fastcar_var = carsvar > 5 and fastcar > 5   
 birthday=str(bdvar)
 print("Your Generation is guessed as: " + birthday)
 fastcar = str(likely_fastcar_var)
 print("Likley to buy a fast car in your lifetime true/or false: "+fastcar)

# Initiate test case, althought no known exceptions caught, still running testing 
 print("Initiating test cases:")  # First input value should be a string
 print("Is name value a string?")
 print(isinstance(namevar, str))
 print("Is birthday year valid?")
 print(bdyearvar > 1901 and bdyearvar < 2020) # Second input should be a valid age of a living person
 print("Is the value to car question a valid datatype?")
 print(isinstance(carsvar, int))



# Initiate program with or without testing based on user selection
if testcase == 1:
     determine_generation_add_testcase()
else:
     determine_generation_no_testcase()
     
