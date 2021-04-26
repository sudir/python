# Sulayman Touray
# Movie Theater Ticket Calculator

# Import sys module for exiting 
import sys

# Prompt for user input of age 
prompt = "Enter your age? For ex. 36\n"
age_var = eval(input(prompt))

# Is movie a 3D movie
movie_3d = input("Is move a 3D movie, type (y) for yes or (n) for no:\n") 


# Price of a movie is $10.00, if its 3d then $15.00 for surcharge

# Check variable "movie_3d" for valid value and assign price accordingly
if movie_3d == "y":
  movie_price_var = 15.00
  moviestatement = "Your movie is 3d: $5.00 surcharge added"
elif movie_3d == "Y":
  movie_price_var = 15.00
  moviestatement = "Your movie is 3d: $5.00 surcharge added"
elif movie_3d == "n":
  movie_price_var = 10.00
  moviestatement = "Your movie is not 3d"
elif movie_3d == "N":
  movie_price_var = 10.00
  moviestatement = "Your movie is not 3d"
else:
  print("Testcase failure detected: invalid yes or no response")
  sys.exit("please try again")



# Computations Needed
# 50% Discount for children and 20% discount for seniors
# Children ages 2 - 12

if 0 <= age_var <= 1:
  print("Testcase failure detected: invalid age, the movies will not accept a child under the age of 2")
  sys.exit("please try again")
elif 2 <= age_var <= 12:
  final_price = (movie_price_var - movie_price_var * 0.5)
  agestatement = "Child discount applied: -50%"
elif 60 <= age_var <= 120:
  final_price = (movie_price_var - movie_price_var * 0.2)
  agestatement = "Seniors discount applied: -20%"
elif age_var > 120:
   print("Testcase failure detected: invalid age")
   sys.exit("please try again")

else:
   # Do nothing, movie price stays normal price depending rather its 3d or not
   final_price = movie_price_var
   agestatement = "No discount applied: 0%"


# Return results
print("Movie cost: $10.00")
print(moviestatement)
print(agestatement)
cost = str(final_price)
print("Final price: "+ cost)

# print white space
x=' ';
print(6*x)
print("Initiating Test Cases:")
if 2 <= age_var <= 120:  # Check age input value accurate 
  print("Valid age? Pass")
else:
  print("Valid age? Fail")
#Check does final price equal correctly computed values  
if final_price == 12.00:
 print("Is final price valid? Pass")
elif final_price == 8.00:
 print("Is final price valid? Pass")
elif final_price == 10.00:
 print("Is final price valid? Pass")
elif final_price == 15.00:
 print("Is final price valid? Pass")
elif final_price == 5.00:
 print("Is final price valid? Pass")
elif final_price == 7.50:
 print("Is final price valid? Pass")
else:
  print("Is final price valid? Fail")





