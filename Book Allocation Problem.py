def ispossible(nums,pages):
    cnt = 1
    s = 0
    for i in nums:
        s+=i
        if s > pages:
            cnt+=1
            s = i
        

    return cnt

def findPages(nums, m):
    n = len(nums)
    if m>n:
        return -1
    l = max(nums)
    r = sum(nums)

    while l<=r:
        mid = (l+r)//2
        if ispossible(nums,mid) > m:
            l=mid+1
        else:
            r=mid-1
    return l

print(findPages(nums = [25, 46, 28, 49, 24], m=4))


