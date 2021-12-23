def calculate_position(commands: str) -> int:
	x = 0
	y = 0
	aim = 0

	for i in commands:
		input = i.split(' ')
		input[1] = int(input[1])
		
		if input[0] == 'forward':
			x += input[1]
			y += input[1]*aim
		elif input[0] == 'down':
			aim += input[1]
		elif input[0] == 'up':
			aim -= input[1]
	
	return x*y

def main():
	commands: str = []
	with open('input.txt', 'r') as input_data:
		for i in input_data:
			commands.append(i.strip())

	pos = calculate_position(commands)

	print(pos)


if __name__ == "__main__":
	main()