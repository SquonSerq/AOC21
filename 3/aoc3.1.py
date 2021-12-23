
def calculate(numbers):
	gamma_number = ''
	epsilon_number = ''

	for i in range(0, len(numbers)):
		if len(numbers[i]) < 12:
			for j in range(len(numbers[i]), 12):
				numbers[i]=''.join([numbers[0], '0'])

	for i in range(0, 12):
		zero_num = 0
		one_num = 0

		for j in numbers:
			if int(j[i]) == 1:
				one_num += 1
			else:
				zero_num += 1
		if one_num > zero_num:
			gamma_number+='1'
			epsilon_number+='0'
		else:
			gamma_number+='0'
			epsilon_number+='1'

	return int(gamma_number, 2)*int(epsilon_number, 2)
	

def main():
	input_data = []
	with open('input.txt', 'r') as input:
		for i in input:
			input_data.append(i.strip())

	num = calculate(input_data)
	print(num)


if __name__ == "__main__":
	main()