def swap(left , right):
    if left > right:
        left , right = right , left


def merge(nums1, m, nums2, n):
   gap = ((m+n)//2)+((m+n)%2)
   
   while gap > 0:
        left = 0 
        right = left + gap
        print(left , right)
        while right < m+n:
            
            if left < m  and right >=m: 
                swap(nums1[left] , nums2[right-m])
                
            elif left >=m:
                swap(nums2[left-m] , nums2[right-m])

            else:
                swap(nums1[left] , nums2[right])
                
            left+=1
            right+=1

        if gap == 1:
            break   
        gap = ((gap)//2)+((gap)%2)


nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)
print(6//2 + 6%2)