class Solution:

    def largestElement(self, arr: list[int]) -> int:
        max_arr = arr[0]
        for num in arr:
            if num > max_arr:
                max_arr = num
        return max_arr

s = Solution()
arr = list(map(int,input("Enter the array elements: ").split()))
k = s.largestElement(arr)

print("The largest element in the array is:", k)

