def calculate_increases(nums: int) -> int:
	increases_number: int = 0
	previous_segment: int = 0

	for i in range(0, len(nums)):
		if i+2 >= len(nums):
			break

		current_segment = nums[i]+nums[i+1]+nums[i+2]

		if previous_segment == 0:
			previous_segment = current_segment
			continue

		if current_segment > previous_segment:
			increases_number+=1

		previous_segment = current_segment

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