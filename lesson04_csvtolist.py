# Challenge level: Beginner

# Goal: Using the code from Lesson 3: File handling and dictionaries, create a function that will open a CSV file and return the result as a nested list.

def csv_to_list(csv_file):
	"Takes a csv file (csv_file) and returns a nested list version of it"
	lines = csv_file.read().split("\n")
	for index, line in enumerate(lines):
		lines[index] = line.split(",")
		#Remove leading and trailing spaces from values
		stripped = []
		for item in lines[index]:
			stripped.append(item.strip())
		lines[index] = stripped
	return lines
	
with open ("survey.csv", "r") as survey_file:
	print csv_to_list(survey_file)
