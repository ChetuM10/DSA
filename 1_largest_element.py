def largestElement(arr):
    max_arr = arr[0]
    for num in arr:
        if num > max_arr:
            max_arr = num
    return max_arr

print(largestElement([3,3,6,1]))