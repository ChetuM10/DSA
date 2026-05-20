class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range (len(nums)):
            needed = target - nums[i] # 9 - 2 = 7
            if needed in seen: #checks if the needed value is present in the seen dictionary
                return [seen[needed], i] #return the index of the needed value and the current index
            seen[nums[i]] = i #add the current value and index to the seen dictionary


s = Solution()
print("Target:", 9)
print("indexes:", s.twoSum([2,7,11,15], 9))