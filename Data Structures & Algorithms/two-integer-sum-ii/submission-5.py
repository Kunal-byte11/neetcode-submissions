class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0

        right = len(nums) - 1

        while left < right :

            currentsum = nums[left] + nums[right]

            if currentsum < target:
                left+=1
            elif currentsum == target:
                return [left+1 , right +1]

            else:
                right-=1
        