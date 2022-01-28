# Set initial state of l-system
initial = "AB"

# Rules for the l-system
rules = {
	"A": "AB",
	"B": "A"
}


def l_system(initial, rules, generation):
	current = initial
	# loop for the number of generations passed in by the arument 'generation'.
	for _ in range(0, generation):
		result = ""
		# gose through the current string character by character to replace each charater with the value
		# stored in the 'rules' lookup table. 
		for state in current:
			result += rules.get(state, state)
		# sets currrent to the result.
		current = result
	return current

# loops 10 times i.e 10 times and prints each generation.
for i in range(0, 10):
	print( "{}: {}".format(i, l_system(initial, rules, i)) )
