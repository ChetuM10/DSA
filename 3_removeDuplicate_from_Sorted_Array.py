class Solution:
    def removeDuplicate(self, nums: list[int]) -> int:
        if not nums:
            return 0

        j = 0
        for i in range (1, len(nums)):
            if nums[j] != nums[i]:
                j = j + 1
                nums[j] = nums[i]

        return j + 1

s = Solution()
nums = list(map(int, input("Enter sorted array with duplicates: ").split()))
k = s.removeDuplicate(nums)

print("Number of unique elements:", k)
print("Modified array:", nums[:k])
