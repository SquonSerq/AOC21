def calculate_increases(nums: int) -> int:
	increases_number = 0
	previous_number = 0
	for i in nums:
		if previous_number == 0:
			previous_number = i
			continue

		if i > previous_number:
			print('in')
			increases_number+=1

		previous_number = i

	return increases_number

def main():
	numbers: int = []
	with open('puzzle1input.txt', 'r') as nums:
		for i in nums:
			numbers.append(int(i.strip()))

	increases_number: int = calculate_increases(numbers)
	print(increases_number)

if __name__ == "__main__":
	main()