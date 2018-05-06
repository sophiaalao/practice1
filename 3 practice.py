


def rectangular_frame(list_of_strings):
	mx = max(list_of_strings, key = len)
	len_of_max = len(mx)
	print("*" * (len_of_max + 2))

	for i in range(0, len(list_of_strings)):
		print("*" + list_of_strings[i] + (" " * (len_of_max - len(list_of_strings[i]))) + "*")

	print("*" * (len_of_max + 2))





strings = ['Hayat', 'Aliyu', 'Gandaye']


rectangular_frame(strings)