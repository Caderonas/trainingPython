def rnaTranscription(dna):
    dna = dna.replace("A", "U")
    dna = dna.replace("T", "A")
    for letter in dna :
        if letter == 'G':
            letter = 'C'
        if letter == 'C':
            letter = 'G'
    print(dna)
    return dna
dna = "GCTAA"
rnaTranscription(dna)