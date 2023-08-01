def findMedian(arr):
# Write your code here
    array = sorted(arr)
    left = []
    right = list(reversed(array))

    for i in range(len(array)):
        if not len(right) == len(left) + 1:
            left.append(array[i])
        right.pop()
    return right[-1]
