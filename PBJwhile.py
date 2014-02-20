# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

print "Goal #1: Write a new version of the PB&J program that uses a while loop.  Print 'Making sandwich #' and the number of the sandwich until you are out of bread, peanut butter, or jelly."
SlicesOfBread1 = input("How many slices of bread? ")
PeanutButter1 = input("How many sandwiches worth of peanut butter? ") 
Jelly1 = input("How many sandwiches worth of jelly? ")
Sandwich1 = 0
while SlicesOfBread1/2>=1 and PeanutButter1 > 0 and Jelly1 > 0:
	SlicesOfBread1 = SlicesOfBread1 - 2
	PeanutButter1 = PeanutButter1 - 1
	Jelly1 = Jelly1 - 1
	Sandwich1 = Sandwich1+1
	print "Making sandwich #{0}".format(Sandwich1)
	if SlicesOfBread1/2 == 1:
		print "I have enough bread for {0} more sandwich, enough peanut butter for {1} more, and enough jelly for {2} more.".format(SlicesOfBread1/2, PeanutButter1, Jelly1)
	else:
		print "I have enough bread for {0} more sandwiches, enough peanut butter for {1} more, and enough jelly for {2} more.".format(SlicesOfBread1/2, PeanutButter1, Jelly1)
		
LimitingIngredients1 = []
if SlicesOfBread1 <= 1:
	LimitingIngredients1.append("bread")
	#print "Added bread to list" //debug
if PeanutButter1 <= 0:
	LimitingIngredients1.append("peanut butter")
if Jelly1 <= 0:
	LimitingIngredients1.append("jelly")
if Sandwich1 >=1:
	#print "SlicesOfBread1 = {0} and PeanutButter1 = {1} and Jelly1 = {2}".format(SlicesOfBread1, PeanutButter1, Jelly1) //debug
	print "All done; I ran out of",
	while len(LimitingIngredients1) >= 2:
		print LimitingIngredients1.pop(),
		print "and",
	print "{0}".format(LimitingIngredients1[0]),
		#print LimitingIngredients1 //debug
		#if Sandwich1 > 1:
		#	print "for {0} sandwiches.".format(Sandwich1)
		#else:
		#	print "for {0} sandwich.".format(Sandwich1)
else:
	print "Couldn't make any sandwiches. I didn't have enough",
	while len(LimitingIngredients1) >= 2:
			print LimitingIngredients1.pop(),
			print "or",
	print "{0}.".format(LimitingIngredients1[0]),
	
# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.
