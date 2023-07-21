def findStrStrIndex(str, substr):
    if substr == "":
        return -1
    
    if len(substr) > len(str):
        return -1
    
    for i in range(len(str) -1 ):
        for j in range(len(substr) - 1):
            if str[i + j] != substr[j]:
                break
            if j == len(substr) - 1:
                return i
    
    return -1 