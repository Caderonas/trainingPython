def atbashCipher(string):
	Plain=  "abcdefghijklmnopqrstuvwxyz"
	Cipher= "zyxwvutsrqponmlkjihgfedcba"
	encrypted=""
	for c in string:
		if c == " ":
			encrypted += " "
		else:
			index = Plain.index(c)
			encrypted += Cipher[index]
	return encrypted