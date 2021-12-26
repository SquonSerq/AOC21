def check_deck(deck):
	for i in range(0, 5):
		line_true_count = 0
		column_true_count = 0
		for j in range(0, 5):
			if deck[i][j]['drawn'] == True:
				line_true_count += 1
			
			if deck[j][i]['drawn'] == True:
				column_true_count += 1

		if line_true_count == 5 or column_true_count == 5:
			sum = 0
			for i in range(0, 5):
				for j in range(0, 5):
					if deck[i][j]['drawn'] == False:
						sum += int(deck[i][j]['number'])

			return sum
	
	return 0

def solve_draw_numbers(numbers, decks):
	win_deck_sum = 0
	decks_local = decks
	for num in numbers:
		next_decks_local = []
		for deck in decks_local:
			for i in range(0, 5):
				for j in range(0, 5):
					if deck[i][j]['drawn'] == True:
						continue
					
					if int(deck[i][j]['number']) == num:
						# print('in')
						deck[i][j]['drawn'] = True

			win_deck_sum = check_deck(deck)
			
			if win_deck_sum > 0:
				if len(decks_local) == 1:
					return win_deck_sum*num
				continue
			else:
				next_decks_local.append(deck)
		
		print(len(next_decks_local))
		decks_local = next_decks_local

def main():
	draw_nums = []
	decks = []
	with open('input.txt', 'r') as input:
		input_arr = []
		for i in input:
			input_arr.append(i)
		draw_nums = input_arr.pop(0).split(',')
		for i in range(0, len(draw_nums)):
			draw_nums[i] = int(draw_nums[i].strip())
		# getting rid of \n after draw nums
		input_arr.pop(0)

		j = 0
		decks.append([])
		for i in input_arr:
			if i == '' or i == '\n':
				j+=1
				decks.append([])
				continue
			
			nums = i.split(' ')
			arr_append = []
			for n in nums:
				if n == '':
					continue
				arr_append.append({
					"number": n.strip(),
					"drawn": False
				})
			
			decks[j].append(arr_append)

		result = solve_draw_numbers(draw_nums, decks)
		print(result)
			

if __name__ == "__main__":
	main()