# Challenge Level: Advanced

# Group exercise!

# Scenario: Your organization has put on three events and you have a CSV with details about those events
#           You have the event's date, a brief description, its location, how many attended, how much it cost, and some brief notes
#           File: https://github.com/shannonturner/python-lessons/blob/master/section_09_(functions)/events.csv

# Goal: Read this CSV into a dictionary.

# Your function should return a dictionary that looks something like this. 
# Bear in mind dictionaries have no order, so yours might look a little different!
# Note that I 'faked' the order of my dictionary by using the row numbers as my keys.

# {0: 
#     {'attendees': '12', 
#     'description': 'Film Screening', 
#     'notes': 'Panel afterwards', 
#     'cost': '$10 suggested', 
#     'location': 'In-office', 
#     'date': '1/11/2014'}, 

# 1: 
#     {'attendees': '12', 
#     'description': 'Happy Hour', 
#     'notes': 'Too loud', 
#     'cost': '0', 
#     'location': 'That bar with the drinks', 
#     'date': '2/22/2014'}, 
# 2: 
#     {'attendees': '200', 
#     'description': 'Panel Discussion', 
#     'notes': 'Full capacity and 30 on waitlist', 
#     'cost': '0', 
#     'location': 'Partner Organization', 
#     'date': '3/31/2014'}
# }


def csv_to_dict(csv_file):
	"Takes a csv file (csv_file) and return a dictionary version of the file with row numbers as main keys"
	lines = csv_file.read().split("\n")
	for index, line in enumerate(lines):
		lines[index] = line.split(",")
		#Remove leading and trailing spaces from values
		stripped = []
		for item in lines[index]:
			stripped.append(item.strip())
		lines[index] = stripped	
	#save the header row as a special list of its own
	headers = lines.pop(0)
	#print "The headers are: ", headers
	#create the dictionary
	dict = {}
	for index, line in enumerate(lines):
		single_line_dict = {}
		#print zip(headers, line)
		for header, element in zip(headers, line):
			#print "header is {0} and element is {1}".format(header, element)
			single_line_dict[header] = element
			#print single_line_dict
		dict[index] = single_line_dict
	return dict

with open ("events.csv", "r") as events_file:
	print csv_to_dict(events_file)
