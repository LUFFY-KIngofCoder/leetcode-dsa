def paint(A, B, C):
    mod = 10000003
    def painters(nums,time):
        cnt = 1
        t = 0
        for i in nums:
            t+=(i)
            if t > time:
                cnt+=1
                t= i
        return cnt
        
    l = max(C)
    r = sum(C)
        
    while l<=r:
        mid = (l+r)//2
        if painters(C,mid,B) > A:
            l = mid+1
        else:
            r=mid-1
    return (l*B)%mod
    
print(paint(A = 10, B = 1, C = [1, 8, 11, 3]))