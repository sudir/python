# Test Case


# List variable where final grade values will be stored
finalGrades = []

# 5 name elements who need to be graded
n = ["Shanika Touray", "Anadontes Touray","Anaïs Touray", "Michael Trotter", "Deborah Trotter"] 

# Are X number of student names in the list the correct number of students 
if len(n) == 5:
    print("Number of students are correct: PASS")
else:
	print("Number of students are correct: FAIL")
# Are student names correct datatype 
if isinstance(n, list):
    print("Datatype of students are correct: PASS")
else:
	print("Datatype of students are correct: FAIL")

# Check if iteration works as intended
# instructions for testing iteration
print("For testing purposes, be sure to enter grade of 100 for Shanika Touray and 100 for Anaïs Touray")
 
for i in n:
   # Clever way to display student name using iteration {} rather than letter i	
   print("Enter a grade for: {}:".format(i))
   # Ensure the input values are type int
   grades = int(input())
   finalGrades.append(grades) # adding the elements

if finalGrades[0] != 100:
    print("Did for loop iterate correctly?: FAIL")
else:
	print("Shanika Touray has the grade expected:\n")
	print(finalGrades[0])
	print("Anaïs Touray has the grade expected\n")
	print(finalGrades[2])
	print("Did for loop iterate correctly?: PASS")

# Are grades correctly converted to int datatypes
if isinstance(grades, int):
    print("Datatype of grades converted to int: PASS")
else:
	print("Datatype of grades converted to int: FAIL")
	


# Is the method used to compute highest max value working?
# test grades for calculation, remember we are only testing the method used
finalGrades = [1, 2, 3, 4, 5, 6] # Max value should return 6, average should return 3.5
if max(finalGrades) == 6:
    print("Does max value calculation method work?: PASS")
else:
	print("Does max value calculation metho work?: FAIL")

# Is the method used to compute average value working?
if sum(finalGrades) / len(finalGrades) == 3.5:
    print("Does average value calculation method work?: PASS")
else:
	print("Does average value calculation metho work?: FAIL")

	
