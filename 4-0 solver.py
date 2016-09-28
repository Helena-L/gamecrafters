def initial_position() :
	return 4

def primitive(pos) :
	if pos == 0 :
		return "LOSE"
	elif pos == 1 or pos == 2 :
		return "WIN"
	else :
		return "UNDECIDED"

def gen_moves(pos) :
	if pos >= 2 :
		return ["take 1", "take 2"]
	elif pos == 1 :
		return ["take 1"]
	else :
		return []

def do_moves(pos, move) :
	if move == "take 1" :
		return pos - 1
	else :
		return pos - 2

def four_to_zero_solver(pos) :
	result = primitive(pos)
	if result != "UNDECIDED" :
		return result
	else :
		result = "LOSE"
		next_list = gen_moves(pos)
		for next_action in next_list :
			next_pos = do_moves(pos, next_action)
			if four_to_zero_solver(next_pos) == "LOSE" :
				result = "WIN"
		return result


# print results for all possible states
i = initial_position()
while i >= 0 :
	print(i, four_to_zero_solver(i))
	i -= 1




