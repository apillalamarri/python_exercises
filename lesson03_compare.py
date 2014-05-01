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
	"Takes a csv file (csv_file) and unique identifier (k) and returns a dictionary version of the file where the main keys are k"
	lines = csv_file.read().split("\n")
	for index, line in enumerate(lines):
		lines[index] = line.split(",")
		#Remove leading and trailing spaces from values
		stripped = []
		for item in lines[index]:
			stripped.append(item.strip())
		lines[index] = stripped	
	#save the header row as a special list of its own - items in this list will be the sub-keys for the dictionary
	headers = lines.pop(0)
	#print "The headers are: ", headers
	#create the dictionary
	dict = {}
	for line in lines:
		single_line_dict = {}
		#print zip(headers, line)
		for header, element in zip(headers, line):
			#print "header is {0} and element is {1}".format(header, element)
			single_line_dict[header] = element
			#print single_line_dict
		dict[single_line_dict.get(k)] = single_line_dict
	return dict

def dict_to_csv (dict, headers):
	csv_string = ""
	for header in headers:
		csv_string +=(header+',')
	csv_string +='\n'
	for v in dict.itervalues():
		for header in headers:
			csv_string += v.get(header)+','
		csv_string +=('\n')
	return csv_string
	
with open ("all_employees.csv", "r") as all_employees_file:
	emp_dict = csv_to_dict(all_employees_file, "email")
	#print "emp_dict is now:"
	#print emp_dict

with open ("survey.csv", "r") as survey_file_for_dict:
	survey_dict = csv_to_dict(survey_file_for_dict, "email")
	#print "survey_dict is now:"
	#print survey_dict
	
with open ("appended_employees.csv", "w") as append_emp:
	append_emp_dict = {}
	for email, info in emp_dict.iteritems():
		single_emp_info = {}
		if survey_dict.get(email):
			print "{0} took the survey! Here is her contact information:".format(emp_dict.get(email).get("name"))
			print "Twitter: {0}".format(survey_dict.get(email).get("twitter"))
			print "Github: {0}".format(survey_dict.get(email).get("github"))
			print "Phone: {0}".format(emp_dict.get(email).get("phone"))
			single_emp_info["name"]=info.get("name")
			single_emp_info["email"]=email
			single_emp_info["phone"]=info.get("phone")
			single_emp_info["department"]=info.get("department")
			single_emp_info["position"]=info.get("position")
			single_emp_info["twitter"]=survey_dict.get(email).get("twitter")
			single_emp_info["github"]=survey_dict.get(email).get("github")
		else:
			single_emp_info["name"]=info.get("name")
			single_emp_info["email"]=email
			single_emp_info["phone"]=info.get("phone")
			single_emp_info["department"]=info.get("department")
			single_emp_info["position"]=info.get("position")
			single_emp_info["twitter"]=""
			single_emp_info["github"]=""
		#print single_emp_info
		append_emp_dict[email]=single_emp_info
	#print append_emp_dict
	headers = ['name', 'email', 'phone', 'department', 'position', 'twitter', 'github']		
	append_emp.write(dict_to_csv(append_emp_dict, headers))
