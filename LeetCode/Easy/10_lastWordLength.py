def lastWordLength(strs):
    i = len(strs) - 1
    length = 0

    while strs[i] == ' ':
        i -= 1

    while i >= 0 and strs[i] != ' ':
        length += 1

    return length