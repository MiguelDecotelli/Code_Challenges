def miniMaxSum(arr):
    minimal_sum = 0
    maximal_sum = 0
    array = sorted(arr)
    
    for number in array[:-1]:
        minimal_sum += number
    
    for number in array[1:]:
        maximal_sum += number
        
    print(f"{minimal_sum} {maximal_sum}")
