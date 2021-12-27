def move(num):
	res = 0
	for i in range(0, num):
		res += i+1
	return res


def calc(data):
	biggest_depth = 0
	for i in data:
		if i > biggest_depth:
			biggest_depth = i

	fuel_consumption = {}
	fuel_consumption['depth'] = 0
	fuel_consumption['consumption'] = 123123123123
	for depth in range(0, biggest_depth+1):
		print(depth)
		fuel = 0

		for level in data:
			fuel += move(abs(depth-level))
		
		if fuel < fuel_consumption['consumption']:
			fuel_consumption['depth'] = depth
			fuel_consumption['consumption'] = fuel
	
	return fuel_consumption



def main():
	data = []
	with open('input.txt', 'r') as f:
		nums = f.read().split(',')
		for i in nums:
			data.append(int(i))

	result = calc(data)
	print(result['depth'])
	print(result['consumption'])
		

if __name__ == "__main__":
	main()