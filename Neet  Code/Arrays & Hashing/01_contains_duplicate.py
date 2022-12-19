def containsDuplicate():
    array = [1,2,3,4,5,6,7,5]

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True

    return False

print(containsDuplicate())
