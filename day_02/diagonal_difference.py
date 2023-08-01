def diagonalDifference(arr):
    # Write your code here
    left_diagonal = []
    right_diagonal = []
    for i in range(len(arr)):
        j = len(arr) - 1 - i
        left_diagonal.append(arr[i][i])
        right_diagonal.append(arr[i][j])
    
    result = abs(sum(left_diagonal) - sum(right_diagonal))
    return result