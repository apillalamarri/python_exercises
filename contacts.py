# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner' },
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}
for name, info in contacts.iteritems():
	print "{0}'s contact information is:".format(name)
	for k,v in info.iteritems():
		print "  {0}: {1}".format(k.title(),v)

# Goal 2:  Display that information as an HTML table.
# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="3"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# ...
# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).


with open ("contact_info.html", "w") as contact_info_code:
	with open ("contacts.csv", "r") as contact_file:
		contacts = contact_file.read().split("\n")
		headers = contacts.pop(0).split(",")
		contact_dict = {}
		for contact in contacts:
			contact_split = contact.split(",")
			single_contact_dict = {}
			for header, element in zip(headers, contact_split):
				single_contact_dict[header] = element
				contact_dict[single_contact_dict.get("Name")] = single_contact_dict
		#print contact_dict
		contact_info_code.write('<table border="1">\n')
		for name, info in contact_dict.iteritems():
			contact_info_code.write('<tr><td colspan="3">\n')
			contact_info_code.write('<b>{0}</b>\n</td>\n</tr>\n'.format(name))
			for k,v in info.iteritems():
				if k != "Name":
					contact_info_code.write('<td>{0}: {1}</td>\n'.format(k.title(),v))
		contact_info_code.write('</tr>\n</table>\n')





	
	
	
	
	
	
