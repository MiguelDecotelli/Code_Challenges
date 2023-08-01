def plusMinus(arr):
    array_size = len(arr)
    pos_ratio = 0
    neg_ratio = 0
    zero_ratio = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            pos_ratio += 1
        elif arr[i] < 0:
            neg_ratio += 1
        else:
            zero_ratio += 1
    positive = f"{pos_ratio/array_size:.6f}"
    negative = f"{neg_ratio/array_size:.6f}"
    zero = f"{zero_ratio/array_size:.6f}"
    print(positive, negative, zero , sep="\n")    
    