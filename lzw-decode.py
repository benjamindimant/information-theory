def decode( input_string ):
	next = ""
	for idx in input_string:
		a = next + dictionary[idx - 1]
		if a in dictionary:
			next = a
		else:
			next = a[len(a)-1]
			dictionary_word = a[0:len(a)-1]	
			dictionary.append(a)
			encoded_version.append(dictionary_word)
	encoded_version.append(next)

encoded_version = []
input_string = [int(x) for x in input("Enter a string to encode: ").split(',')]
dictionary = input("Enter a dictionary: ").split(',')
decode(input_string)
print("The final dictionary is: ", dictionary)
print("The decoded version of the encoded string is: ", ''.join(encoded_version))

