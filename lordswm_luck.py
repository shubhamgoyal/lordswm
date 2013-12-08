import itertools

TOTAL_TURNS = 10
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
	return F**(1 + turns_befallen - (turn_number - turns_befallen - 1)*F/(1 - F))

def get_prob_sequence(sequence):
	final_prob = 1.0
	num_previous_luck_falls = 0
	for i in range(1, TOTAL_TURNS + 1):
		element = sequence[i - 1]
		if element == 'l':
			final_prob *= get_prob(LUCK, i, num_previous_luck_falls)
			num_previous_luck_falls += 1
		elif element == 'u':
			final_prob *= (1 - get_prob(LUCK, i, num_previous_luck_falls))
		else:
			print "Something is not right"
	# print sequence
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
		total_prob += get_prob_sequence(permuted_sequence)
	return total_prob

lucky_times = 0.0
for i in range(1, TOTAL_TURNS + 1):
	lucky_times += i * get_prob_luck_falls_x_times(i)

print lucky_times