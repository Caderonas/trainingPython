def rnaTranscription(dna):
    """ Convert dna to rna."""
    mapping = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
    rna = ''
    for char in dna:
        rna += mapping[char]
    print (rna)
    return rna