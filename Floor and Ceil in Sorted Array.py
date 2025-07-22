def getFloorAndCeil(nums, target):
    mid = 0
    n = len(nums)
    l = 0
    r = n-1
    while l<=r :
        mid = (l+r)//2
        if nums[mid] == target:
            return nums[mid] , nums[mid]
        elif nums[mid] > target:
            r= mid-1
        else:
            l= mid+1
    
    if nums[mid]>target:
        ceil = nums[mid]
        if mid!= 0:
            floor = nums[mid-1]
        else:
            floor = -1
            
    elif nums[mid]<target:
        floor = nums[mid]
        ceil = -1
        
    return floor,ceil

print(getFloorAndCeil([3, 4, 4, 7, 8, 10],7))
