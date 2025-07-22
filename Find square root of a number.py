def floorSqrt1(n):
    if n == 0:
        return n
    #print(n//2)
    nums = list(i  for i in range(1,(n//2)+1))
    l = 0
    r = len(nums)-1
    ans = 1
    mid = 0
    #print(nums)
    while l<=r:
        mid = (l+r)//2
        #print(nums[mid],mid,l ,r)
        if nums[mid]**2 == n:
            return nums[mid]
        elif nums[mid]**2 < n:
            ans = nums[mid]
            l = mid+1
        else:
            r = mid-1
        
    return ans

def floorSqrt2(n):
    if n == 0:
        return 0

    l = 1
    r = (n//2)+1
    ans = 1
    while l<=r:
        mid = (l+r)//2
        if mid**2 == n:
            return mid
        elif mid**2 < n:
            ans = mid
            l = mid+1
        else:
            r = mid-1
    return ans
    

print(floorSqrt2(37))
