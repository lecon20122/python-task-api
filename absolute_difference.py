def absoluteValue(array):
    array.sort()
    for i in range(len(arr)-1):
        diff = abs(array[i] - array[i+1])
    return diff


arr = [3, -7, 0]
print(absoluteValue(arr))
