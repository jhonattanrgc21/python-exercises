def count_vowels(cad):
	count_a = 0
	count_e = 0
	count_i = 0
	count_o = 0
	count_u = 0

	for letter in cad:
		if(letter == 'a'):
			count_a += 1
		
		if(letter == 'e'):
			count_e += 1

		if(letter == 'i'):
			count_i += 1

		if(letter == 'o'):
			count_o += 1
		
		if(letter == 'u'):
			count_u += 1

	print('A:\t{}\t{}'.format(count_a ,'*' * count_a))
	print('E:\t{}\t{}'.format(count_e ,'*' * count_e))
	print('I:\t{}\t{}'.format(count_i ,'*' * count_i))
	print('O:\t{}\t{}'.format(count_o ,'*' * count_o))
	print('U:\t{}\t{}'.format(count_u ,'*' * count_u))


def main():
	cad = input()
	count_vowels(cad)

if(__name__ == '__main__'):
	main()