class Solution:
    def check(self, nums: List[int]) -> bool:
        # a = nums.index(min(nums))
        # i = a+1
        # while (i != a): 
        #     if i == len(nums):
        #         i = 0     
        #     if i == 0:
        #         if nums[i] < nums[len(nums)-1]:
        #             return False
        #             break
        #     else:
        #         if nums[i] < nums[i-1]:
        #             return False
        #             break
        #     i+=1
        #     if i == len(nums):
        #         i = 0 

        # return True
        a = sorted(nums)
        for x in range(len(nums)):
            i = 0
            for i in range(len(nums)):
                if nums[i] != a[(i+x) % len(a)]:
                    break
                i+=1
            if i == len(a):
                return True
                break
        
        return False
