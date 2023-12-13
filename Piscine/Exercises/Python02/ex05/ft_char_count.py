import sys
argc = len(sys.argv)
if argc < 2:
	print("Error! No string given")
else:
	str = sys.argv[1].lower()
	list = []
	i = 0
	count = 0
	while i < len(str):
		j = 0
		count = 0
		while j < len(str):
			if str[j] == str[i]:
				count += 1
			j += 1
		list.append((str[i], count))
		i += 1
	i = 0
	while i < len(list):
		j = i
		while j < len(list):
			if list[i][0] > list[j][0]:
				list[i], list[j] = list[j], list[i]
			j += 1
		i += 1
	dct = dict(list)
	for key, value in dct.items():
		print(key, "=", value)
