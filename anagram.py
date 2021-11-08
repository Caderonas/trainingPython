def anagram(base, listWords):
    output = []
    for word in listWords:
        if sorted(base) == sorted(word):
            output.append(word)
    return output