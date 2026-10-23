class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        distinctNums = {}

        for i in nums:
            if i in distinctNums:
                distinctNums[i] += 1
            else:
                distinctNums[i] = 1
        
        for j in distinctNums:
            if distinctNums[j] > len(nums) / 2:
                return j
                