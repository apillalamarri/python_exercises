# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).  
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py
# Challenge 2: Save the HTML as states.html instead of printing it to screen.  
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

with open("states.txt", "r") as states_file:
	states = states_file.read().split("\n")

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

with open("state_info.csv", "r") as  state_info_file:
	state_info = state_info_file.read().split("\n")
header = state_info.pop(0).split(",")
#print header

with open("stateinfo.html", "w") as state_info_code:
	state_info_code.write('<select>\n')
	for index, state in enumerate(states):
		states[index] = state.split("\t")
		state_info_code.write('\t<option value="{0}">{1}</option>\n'.format(states[index][0], states[index][1]))
	state_info_code.write('</select>\n')
	for state in state_info:
		state = state.split(",")
		state_info_code.write('<a name={0}></a>\n'.format(state[1]))
		state_info_code.write('<table border="1">\n<tr>\n<td colspan="2">\n')
		state_info_code.write('<b>'+state[1].replace('"','') + '</b>\n</td>\n</tr>\n<tr>')
		state_info_code.write('<td> Rank: ' + state[0] + '</td>\n')
		state_info_code.write('<td> Percent: '+ state[4].replace('"','') +'</td>\n</tr>\n<tr>\n')
		state_info_code.write('<td> US House Members: '+ state[3] +'</td>\n')
		state_info_code.write('<td> Population: '+ state[2] +'</td>\n</tr>\n</table><br>\n')
		
# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>
