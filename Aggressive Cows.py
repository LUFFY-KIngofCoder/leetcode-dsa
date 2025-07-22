def can_we_place(nums, dist,k):
    cnt_Cows = 1
    last = 0
    i = 1
    while cnt_Cows < k and i < len(nums):
        if nums[i] - nums[last] >= dist:
            last = i
            cnt_Cows +=1
        i+=1
        if cnt_Cows == k:
            return True
    return False


def aggressiveCows(nums, k):
    nums.sort()
    n = len(nums)
    l = 1
    r = nums[n-1] - nums[0]
    
    while l<=r:
        mid = (l+r)//2
        
        if can_we_place(nums, mid, k):
            l = mid+1
        else:
            r=mid-1
    
    return r
    
print(aggressiveCows([0, 3, 4, 7, 10, 9],4))