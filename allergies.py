def allergies (allergie):
	allergies = ["egs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]
	outputs = []
	for i in range(len(allergies)-1, 0, -1):
		if allergie >= 2**i:
			outputs.append(allergies[i])
		allergie -= 2**i if 2**i <= allergie else 0
	print (outputs)
	return outputs

allergies(34)