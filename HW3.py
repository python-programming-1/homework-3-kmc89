num = 0

try:
	num_input = input('Enter a number: ')

except:
	print('Invalid input!')

num = int(num_input)

def collatz(num):
	if (num)%2 == 0:
		col_num = int(num /2)
		print(col_num)
		return (col_num)
	else:
		col_num = num * 3 + 1
		print(col_num)
		return (col_num)

while num > 1:
	num = collatz(num)

