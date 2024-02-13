def search2dMatrix(array2D, target):
    #time complexity= O(m * log(n))
    for i in range(len(array2D)): # O(m) for rows or nested array.
        left = 0 
        right = len(array2D[i]) - 1
        
        if array2D[i][right] >= target:
            while left <= right: # O(log(n)) binary search for elements in each nested array.
                midValue = (left + right) // 2
                    
                if array2D[i][midValue] == target:
                    return [i, midValue]
                elif array2D[i][midValue] < target:
                    left = midValue + 1
                else:
                    right = midValue - 1
                
    return "Target Not Found!"

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search2dMatrix(matrix, 11))
