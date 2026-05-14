class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = (
                    nums[right],
                    nums[left],
                )  # Swap left and right elements
                left += 1  # move left pointer forward
                right -= 1  # move right pointer backward

        reverse(0, n - 1)  # reverse whole array
        reverse(0, k - 1)  # reverse first k elements
        reverse(k, n - 1)  # reverse remaining elements


s = Solution()
arr = list(map(int, input("Enter the array elements: ").split()))
k = int(input("Enter the number of rotations: "))
s.rotate(arr, k)
print("The rotated array is:", arr)
