def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)
    
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            result[prev_index] = i - prev_index
        stack.append(i)
    
    return result

# Example usage:
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]

result1 = dailyTemperatures(temperatures1)


print(f"Input: {temperatures1}")
print(f"Output: {result1}")
