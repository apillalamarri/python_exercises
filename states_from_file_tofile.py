with open("states.csv", "r") as states_file:
        states = states_file.read().split("\n")

with open("statedropdown.html", "w") as state_dropdown_code:
    state_dropdown_code.write('<select>')
    for index, state in enumerate(states):
        states[index] = state.split(",")
        #print '\t<option value="{0}">{1}</option>'.format(states[index][0], states[index][1])
        state_dropdown_code.write('\t<option value="{0}">{1}</option>'.format(states[index][0], states[index][1]))
    state_dropdown_code.write('</select>')
