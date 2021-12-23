
def calculate_first(numbers):
	result = ''
	check_nums = numbers
	for i in range(0, 13):
		if len(check_nums) == 1:
			result = check_nums[0]
			break
		
		one_nums = 0
		zero_nums = 0 
		for j in check_nums:
			if int(j[i]) == 1:
				one_nums += 1
			else:
				zero_nums += 1
		
		next_check_nums = []
		for j in check_nums:
			if one_nums >= zero_nums:
				if int(j[i]) == 1:
					next_check_nums.append(j)
			else:
				if int(j[i]) == 0:
					next_check_nums.append(j)

		check_nums = next_check_nums

	return result

def calculate_second(numbers):
	result = ''
	check_nums = numbers
	for i in range(0, 13):
		if len(check_nums) == 1:
			result = check_nums[0]
			break
		
		one_nums = 0
		zero_nums = 0 
		for j in check_nums:
			if int(j[i]) == 1:
				one_nums += 1
			else:
				zero_nums += 1
		
		next_check_nums = []
		for j in check_nums:
			if one_nums >= zero_nums:
				if int(j[i]) == 0:
					next_check_nums.append(j)
			else:
				if int(j[i]) == 1:
					next_check_nums.append(j)

		check_nums = next_check_nums

	return result
	

def main():
	input_data = []
	with open('input.txt', 'r') as input:
		for i in input:
			input_data.append(i.strip())

	for i in range(0, len(input_data)):
		if len(input_data[i]) < 12:
			for j in range(len(input_data[i]), 12):
				input_data[i]=''.join([input_data[0], '0'])

	num1 = calculate_first(input_data)
	num2 = calculate_second(input_data)

	print(int(num1,2))
	print(int(num2,2))
	print(int(num1, 2)*int(num2,2))


if __name__ == "__main__":
	main()