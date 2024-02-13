def plusMinus(arr):
    total = len(arr)
    positive_count = sum(1 for num in arr if num > 0)
    negative_count = sum(1 for num in arr if num < 0)
    zero_count = total - positive_count - negative_count
    
    positive_ratio = positive_count / total
    negative_ratio = negative_count / total
    zero_ratio = zero_count / total
    
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

# Example usage:
arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
