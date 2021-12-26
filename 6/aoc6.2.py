def find_fish_number(init_fish, days):
	fishes = [0 for x in range(0, 9)]

	for i in init_fish:
		fishes[i]+=1

	for i in range(0, days):
		new_fishes = [0 for x in range(0, 9)]
		for j in range(0, 9):
			if j == 0:
				new_fishes[6] += fishes[0]
				new_fishes[8] += fishes[0]
				continue
			
			new_fishes[j-1] += fishes[j]
		fishes = new_fishes

	sum = 0
	for i in fishes:
		sum += i

	return sum

def main():
	data = []
	with open('input.txt', 'r') as f:
		nums = f.read().split(',')
		for i in nums:
			data.append(int(i))

	result = find_fish_number(data, 256)
	print(result)

if __name__ == "__main__":
	main()