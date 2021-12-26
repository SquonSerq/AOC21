class Fish:
	def __init__(self, days):
		self.days = days
	
	def check_cycle(self, arr):
		if self.days == 0:
			self.days = 6
			arr.append(Fish(days=9))
		else:
			self.days-=1

def find_fish_number(init_fish, days):
	fishes = init_fish
	for i in range(0, days):
		next_day_fishes = fishes
		for fish in fishes:
			fish.check_cycle(next_day_fishes)
		
		fishes = next_day_fishes

	return len(fishes)

def main():
	data = []
	with open('input.txt', 'r') as f:
		nums = f.read().split(',')
		for i in nums:
			data.append(Fish(int(i)))

	result = find_fish_number(data, 256)
	print(result)

if __name__ == "__main__":
	main()