def diagonalDifference(arr):
    n = len(arr)  # Number of rows or columns in the square matrix
    left_to_right_sum = sum(arr[i][i] for i in range(n))
    right_to_left_sum = sum(arr[i][n - 1 - i] for i in range(n))
    absolute_difference = abs(left_to_right_sum - right_to_left_sum)
    return absolute_difference

# Example usage:
if __name__ == "__main__":
    # Input: 3x3 square matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [9, 8, 9]
    ]
    result = diagonalDifference(matrix)
    print(result)
