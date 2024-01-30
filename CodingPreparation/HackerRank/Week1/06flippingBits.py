def flippingBits(n):
    # 32-bit mask with all bits set to 1
    mask = 2**32 - 1
    
    # Flip all bits using XOR with the mask
    result = n ^ mask
    
    return result

if __name__ == '__main__':
    q = int(input().strip())  # Number of queries

    for _ in range(q):
        n = int(input().strip())  # Integer to process
        result = flippingBits(n)
        print(result)
