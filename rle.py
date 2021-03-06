def rle(string):
    """ Convert each multiple
        char in a row by the number of
        occurence follow by the char.
        Recursively
        Output : print
    """
    if len(string) == 0:
        print ("")
        return ""
    curLetter = string[0]
    count = 0
    while string[0] == curLetter:
        count += 1
        string = string.replace(curLetter, "", 1)
        if len(string) == 0:
            break
    if count == 1:
        print(curLetter, end="")
    else:
        print (str(count) + curLetter, end="")
    if len(string) > 1:
        rle(string)
    else:
        print(string)

rle("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB")