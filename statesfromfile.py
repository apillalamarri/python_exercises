with open("states.csv", "r") as states_file:
        states = states_file.read().split("\n")
print '<select>'
for index, state in enumerate(states):
        states[index] = state.split(",")
        print '\t<option value="{0}">{1}</option>'.format(states[index][0], states[index][1])
print '</select>'
