def main():
	import pickle
	with open('words.txt', 'r') as file:
		lines = file.readlines()
		print(lines)
		dct = dict()
		for line in lines:
			dct[len(line) - 1] = dct.get(len(line) - 1, 0) + 1
		with open('word_count.pickle', 'wb') as file2:
			pickle.dump(dct, file2)

if __name__ == "__main__":
	main()
