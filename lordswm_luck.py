TOTAL_TURNS = 14
LUCK = 2

class unique_element:
    def __init__(self,value,occurrences):
        self.value = value
        self.occurrences = occurrences

def perm_unique(elements):
    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)

def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1

def get_prob(luck, turn_number, turns_befallen):
	F = min(0.5, luck/10.0)
	prob = F**(1 + turns_befallen - (turn_number - turns_befallen - 1)*F/(1 - F))
	# if prob > 1:
	# 	print "Probability greater than 1: prob = ", prob, " luck = ", luck, " turn_number = ", turn_number, " turns_befallen = ", turns_befallen
	return prob

def get_prob_sequence(sequence, num_luck_falls):
	final_prob = 1.0
	num_previous_luck_falls = 0
	for i in range(1, TOTAL_TURNS + 1):
		element = sequence[i - 1]
		prob = get_prob(LUCK, i, num_previous_luck_falls)
		if prob > 1.0:
			return 0.0
		elif element == 'l':
			final_prob *= prob
			num_previous_luck_falls += 1
		elif element == 'u':
			final_prob *= (1.0 - prob)
		else:
			print "Something is not right"
	# print sequence
	# print final_prob
	if final_prob == 1.0:
		print "Control didn't enter the for loop in get_prob_sequence"
	# print final_prob
	return final_prob

def get_prob_luck_falls_x_times(x):
	total_prob = 0.0
	sequence_falls = []
	for i in range(0, x):
		sequence_falls.append('l')
	for i in range(x, TOTAL_TURNS):
		sequence_falls.append('u')
	for permuted_sequence in perm_unique(sequence_falls):
		# print permuted_sequence
		total_prob += get_prob_sequence(permuted_sequence, x)
	return total_prob

# sum = 0.0
# for i in range(0, TOTAL_TURNS + 1):
# 	sum = sum + get_prob_luck_falls_x_times(i)
# 	print i, " = ", get_prob_luck_falls_x_times(i)
# print "sum = ", sum
lucky_times = 0.0
for i in range(1, TOTAL_TURNS + 1):
	lucky_times += i * get_prob_luck_falls_x_times(i)

print lucky_times