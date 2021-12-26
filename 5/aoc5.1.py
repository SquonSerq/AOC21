class Line:
	def __init__(self, x1, y1, x2, y2):
		self.x = [x1, x2]
		self.y = [y1, y2]

def solve_lines(lines):
	area = [[0 for j in range(0, 1000)] for i in range(0, 1000)]

	for line in lines:
		if line.x[0] == line.x[1]:
			if line.y[0] < line.y[1]:
				for i in range(line.y[0], line.y[1]+1):
					area[line.x[0]][i] += 1
			else:
				for i in range(line.y[1], line.y[0]+1):
					area[line.x[0]][i] += 1
		elif line.y[0] == line.y[1]:
			if line.x[0] < line.x[1]:
				for i in range(line.x[0], line.x[1]+1):
					area[i][line.y[0]] += 1
			else:
				for i in range(line.x[1], line.x[0]+1):
					area[i][line.y[0]] += 1


	# print(area)
	crosses = 0
	for line in area:
		for num in line:
			if num > 1:
				crosses+=1
	
	return crosses

def main():
	lines = []
	with open('input.txt', 'r') as input:
		for line in input:
			coords = line.split(' -> ')
			xy1 = coords[0].split(',')
			xy2 = coords[1].split(',')
			lines.append(Line(int(xy1[0]), int(xy1[1]), int(xy2[0]), int(xy2[1])))

	crosses = solve_lines(lines)
	print(crosses)


if __name__ == "__main__":
	main()