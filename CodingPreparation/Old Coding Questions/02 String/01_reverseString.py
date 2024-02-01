#Reverse a String.
def reverseString1(strin):
    return strin[::-1]

def reverseString2(strin):
    str_list = list(strin)
    
    j = len(str_list) - 1
    for i in range(len(str_list)//2):
        str_list[i], str_list[j] = str_list[j], str_list[i]
        j -= 1
        
    return ''.join(str_list)

# Example usage:
input_str = "hello"
result = reverseString2(input_str)
print(result)
