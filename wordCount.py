def countWord(sentence):
    words = sentence.split()
    if (len(words) == 0):
        return
    count = 0
    while sentence.find(words[0]) != -1:
        sentence = sentence.replace(words[0], "", 1);
        count += 1
    countStr = str(count)
    print(words[0]+' '+ countStr)
    countWord(sentence)

sentence = "olly olly in come free"
countWord(sentence)