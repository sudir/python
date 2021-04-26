
# Written by: Sulayman Touray
# Introduction to Problem Solving & Algorithm Design
# Calculating Quiz Grades
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

# List variable where final grade values will be stored
finalGrades = []

# 5 name elements who need to be graded
n = ["Shanika Touray", "Anadontes Touray","Anaïs Touray", "Michael Trotter", "Deborah Trotter"] 

# grading instructions for instructor
print("Enter a grade value for each student between 1 - 100")
# iterating for each name represented by letter i
for i in n:
   # Clever way to display student name using iteration {} rather than letter i	
   print("Enter grade number for {}:".format(i))
   # Ensure the input values are type int
   grades = int(input())
   finalGrades.append(grades) # adding the elements
print("The highest grade given was:\n", max(finalGrades)) # here we call the max function learned in week 4/5 to find highest value
print("The average of all grades provided was:\n", sum(finalGrades) / len(finalGrades)) # here we call the sum and len functions to find average