def encode( input_string ):
	next = ""
	for char in input_string:
		a = next + char
		if a in dictionary:
			next = a
		else:
			next = a[len(a)-1]
			dictionary_word = a[0:len(a)-1]	
			dictionary.append(a)
			encoded_version.append(dictionary.index(dictionary_word))
	encoded_version.append(dictionary.index(next))

def decodeLzw( encoded_version ):
	x = ""	
	for i in encoded_version:
		x = x + dictionary[i]
	return x

encoded_version = []
input_string = input("Enter a string to encode: ")
dictionary = input("Enter a dictionary: ").split(',')
encode(input_string)
decoded_version = decodeLzw(encoded_version)
print("The encoded version of the given string is: ", [int(x) + 1 for x in encoded_version])
print("The final dictionary is: ", dictionary)
print("The decoded version of the encoded string is: ", decoded_version)
