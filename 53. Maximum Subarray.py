class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        now = 0
        n = len(nums)
        j= 0
        for i in range(n):
            now += nums[i]
            maxi = max(now , maxi)
            if now < 0:
               now = 0         

        return maxi 
