# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.


# What are the step-by-steps to recreate this?
# First, you need variables to store your information.  Remember, variables are just containers for your information that you give a name.

# You need three ingredients to make a PB&J, so you'll want three different variables:
# 		How much bread do you have? (make this a number that reflects how many slices of bread you have)
print "Let's take an inventory of our peanut butter and jelly sandwich supplies."
SlicesOfBread = input('How many slices of bread do I have? ')
#		How much peanut butter do you have? (make this a number that reflects how many sandwiches-worth of peanut butter you have)
SandwichesWorthOfPB = input('How many sandwiches worth of peanut butter do I have? ')
#		How much jelly do you have? (make this a number that reflects how many sandwiches-worth of jelly you have)
SandwichesWorthOfJelly = input('How many sandwiches worth of jelly do I have? ')
print ""
# For this exercise, we'll assume you have the requisite tools (plate, knife, etc)

# Once you've defined your variables that tell you how much of each ingredient you have, use conditionals to test whether you have the right amount of ingredients

# Based on the results of that conditional, display a message.

# To satisfy the first goal:

#		If you have enough bread (2 slices), peanut butter (1), and jelly (1), print a message like "I can make a peanut butter and jelly sandwich"; 
#		If you don't; print a message like "Looks like I don't have a lunch today"
print "1. Can I make a peanut butter and jelly sandwich?"
EnoughBread = SlicesOfBread >= 2
EnoughPB = SandwichesWorthOfPB >=1
EnoughJelly = SandwichesWorthOfJelly >=1
if EnoughBread and EnoughPB and EnoughJelly :
	print "I can make a peanut butter and jelly sandwich."
else:
	print "Looks like I don't have a lunch today."
print ""
# To satisfy the second goal:
#		Continue from the first goal, and add:
#		If you have enough bread (at least 2 slices), peanut butter (at least 1), and jelly (at least 1), print a message like "I can make this many sandwiches: " and then calculate the result.
#		If you don't; you can print the same message as before
print "2. How many peanut butter and jelly sandwiches can I make?"
SandwichesWorthOfBread = SlicesOfBread/2
PossibleNumberOfSandwiches = min(SandwichesWorthOfBread, SandwichesWorthOfPB, SandwichesWorthOfJelly)
if SlicesOfBread >= 2 and SandwichesWorthOfPB >= 1 and SandwichesWorthOfJelly >=1:
	#print "I have {0} sandwiches worth of bread.".format(SandwichesWorthOfBread)
	print "I can make {0} peanut butter and jelly sandwiches.".format(PossibleNumberOfSandwiches)
	CanMakeSandwich = True
else:
	CanMakeSandwich = False
	print "Looks like I don't have a lunch today."
print ""
# To satisfy the third goal:
#		Continue from the second goal, and add:
#		If you have an odd number of slices of bread* and odd amount of peanut butter and jelly, print a message like before, but mention that you can make an open-face sandwich, too.
#		If you don't have enough ingredients; still print the same message as before
#		* To calculate whether you have an odd number, see https://github.com/shannonturner/python-lessons/blob/master/section_01%20%28basics%29/simple_math.py
print "3. Can I make an open-face sandwich after I make all possible closed sandwiches?"
if CanMakeSandwich == True:
	if SlicesOfBread%2 !=0 and SandwichesWorthOfJelly%2 !=0 and SandwichesWorthOfPB%2 !=0:
		print "I can make an additional open-face sandwich."
	else:
		print "Nope, no open-faced sandwiches can be made."
elif SlicesOfBread%2 !=0 and SandwichesWorthOfJelly%2 !=0 and SandwichesWorthOfPB%2 !=0:
	print "I can only make an open-face sandwich."
else:
	print "Looks like I don't have a lunch today."
print ""
# To satisfy the fourth goal:
#		Continue from the third goal, but this time if you don't have enough ingredients, print a message that tells you which ones you're missing.
print "4. Do I need more of anything to make a peanut butter and jelly sandwich?"
if not EnoughBread:
	print "I need more bread."
if not EnoughPB:
	print "I need more peanut butter."
if not EnoughJelly:
	print "I need more jelly."
if EnoughBread and EnoughPB and EnoughJelly:
	print "Nope, I'm all set."
print ""
# To satisfy the fifth goal:
#		Continue from the fourth goal, but this time if you have enough bread and peanut butter but no jelly, print a message that tells you that you can make a peanut butter sandwich
#		Or if you have more peanut butter and bread than jelly, that you can make a certain number of peanut butter & jelly sandwiches and a certain number of peanut butter sandwiches
print "5. If I run out of jelly and I'm desperate, can I make a peanut butter sandwich?"
if EnoughBread and EnoughPB and not EnoughJelly:
	print "There's no jelly, but I can make a peanut butter sandwich."
else:
	print "Yes, I can make a peanut butter sandwich."
BreadOverage = SandwichesWorthOfBread - PossibleNumberOfSandwiches
PBOverage = SandwichesWorthOfPB - PossibleNumberOfSandwiches
PBSandwiches = min(BreadOverage, PBOverage)
if SandwichesWorthOfBread > SandwichesWorthOfJelly and SandwichesWorthOfPB > SandwichesWorthOfJelly:
	print "I can make {0} peanut butter and jelly sandwiches.".format(PossibleNumberOfSandwiches)
	print "I can make {0} peanut butter sandwiches.".format(PBSandwiches)
else:
	print "I won't run out of jelly and have extra peanut butter."