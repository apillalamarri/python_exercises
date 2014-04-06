# Challenge Level: Advanced

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You took a survey of all of the employees at your organization to see what their twitter and github names were. You got a few responses.
#   You have two spreadsheets in CSV (comma separated value) format:
#       all_employees.csv: See section_07_(files).  Contains all of the employees in your organization and their contact info.
#           Columns: name, email, phone, department, position
#       survey.csv: See section_07_(files).  Contains info for employees who have completed a survey.  Not all employees have completed the survey.
#           Columns: email, twitter, github

# Challenge 1: Open all_employees.csv and survey.csv and compare the two.  When an employee from survey.csv appears in all_employees.csv, print out the rest of their information from all_employees.csv.

# Sample output:
#       Shannon Turner took the survey! Here is her contact information: Twitter: @svt827 Github: @shannonturner Phone: 202-555-1234

def csv_to_dict(csv_file, k):
	lines = csv_file.read().split("\n")
	headers = lines.pop(0).split(",")
	dict = {}
	for line in lines:
		line_split = line.split(",")
		single_line_dict = {}
		for header, element in zip(headers, line_split):
			single_line_dict[header] = element
			dict[single_line_dict.get(k)] = single_line_dict
	return dict

with open ("all_employees.csv", "r") as all_employees_file:
	emp_dict = csv_to_dict(all_employees_file, "name")
with open ("survey.csv", "r") as survey_file:
	survey_dict = csv_to_dict(survey_file, "email")
	
for email, info in survey_dict.iteritems():
	for name, emp in emp_dict.iteritems():
		print emp
		print "\n"
		#if email == emp.get('email'):
		#	print "{0} took the survey! Here is her contact information: ".format(name),
		#	for k, v in emp.iteritems():
		#		print "{0}: {1}".format(k, v),
		#	print "\n"
# Challenge 2: Add the extra information from survey.csv into all_employees.csv as extra columns.  
# IMPORTANT: It would probably be a good idea to save it as an extra file instead of accidentally overwriting your original!
# By the end, your all_employees.csv should contain the following columns: name, email, phone, department, position, twitter, github
