import string
def pangram(sentence):
    """ Define if the 
        sentence(string)
        is a pangram or not.
    """
    alphabet = list(string.ascii_lowercase)
    sentence = sentence.lower()
    for letter in alphabet:
        isIn = sentence.find(letter)
        if isIn == -1:
            return False
    return True