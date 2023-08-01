def countingSort(arr):
    new_array = [0] * 100

    for i in range(len(arr)):
        new_array[arr[i]] += 1
    return new_array




