
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

# Adding 3 carpet types. Prices are (standard - $5.00 per sqft),  (medium - $10.00 per sqft), and (premium - $20.00 per sqft)
cpgrade = input("Hello, please type the grade of carpet you would like:\n (standard) - $5.00 per sqft.\n  (medium) - $10.00 per sqft.\n  (premium) - $20.00 per sqft\n" )
# Take input of feet
cpft = eval(input("Enter how the number of feet you'd like:\n"))
# Take input of length to calculate square footage
cplh = eval(input("Enter in the number of length\n"))


# function to calculate input values passed as parameters
def calculate_carpet_total(cpgrade, cpft, cplh):

 if   cpgrade == "standard":
      cost = (cpft * cplh * 5.00)
      print("Standard carpet was selected for a total price of:\n")
      print(cost)
 elif cpgrade == "medium":
      cost = (cpft * cplh * 10.00)
      print("Medium carpet was selected for a total priceof:\n")
      print(cost)
 elif cpgrade == "premium":
      cost = (cpft * cplh * 20.00)
      print("Premium carpet was selected for a total priceof:\n")
      print(cost)


# Call the function
calculate_carpet_total(cpgrade, cpft, cplh)