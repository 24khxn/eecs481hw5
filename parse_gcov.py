import math
total_num_lines = 0
lines_covered = 0

with open('all_percentages.output', 'r') as file:
	lines = file.read().split('\n')
	for line in lines:
		if not line: continue
		# print(line)
		x = line.split('Lines executed:')[1].split(' of ')
		percentage = float(x[0].split('%')[0])
		total_lines = int(x[1])
		# print(percentage)
		# print(total_lines)
		total_num_lines += total_lines
		lines_covered += total_lines * (percentage * 0.01)

# print('Total lines covered: {} out of {}'.format(lines_covered, total_num_lines))
y = lines_covered / total_num_lines
y *= 10000
y = math.floor(y)
print(y)

