35.Two Sum
Approach: Hash map

Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]=i

--------------------------------------------------------------------------------------

Wrong Approach: Two pointers ( Wrong because 2 pointers only work for sorted arrays )

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        while(low<high):
            if (nums[low]+nums[high]==target):
                return [low,high]
            elif (nums[low]+nums[high])>target:
                high=high-1
            else:
                low=low+1