class Solution:
    def check(self, nums: list[int]) -> bool:
        count = 0

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count += 1

        if nums[0] < nums[-1]:
            count += 1

        return count <= 1


s = Solution()
print(s.check([1,2,3,4,5]))
print(s.check([3,4,5,1,2]))
print(s.check([1,1,1]))
print(s.check([2,1,3,4]))