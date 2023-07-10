def palindrome(self, num:int):

    if num < 0:
        return False
    
    div = 1

    while num > div:
        div *= 10
    
    while num:
        right = num % 10
        left = num // div

        if right != left:
            return False
    
        num = (num % div) // 10
        div = div / 100 # divide by 100 because we removed left and right digits. 

    return True