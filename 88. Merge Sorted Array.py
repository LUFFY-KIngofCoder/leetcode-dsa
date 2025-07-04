def swap(arr1 , arr2 ,left , right):
    if arr1[left] > arr2[right]:
        arr1[left] , arr2[right] = arr2[right] , arr1[left]


def merge(nums1, m, nums2, n):
    gap = ((m+n)//2)+((m+n)%2)
   
    while gap > 0:
        left = 0 
        right = left + gap

        print(left , right ,gap)
        while right < m+n:

            if left < m  and right >=m: 
                swap(nums1,nums2, left,right-m)
                
            elif left >=m:
                swap(nums2,nums2  ,left-m ,right-m)

            else:
                swap(nums1, nums2,left ,right)

                
            left+=1
            right+=1

        if gap == 1:
            break   
        gap = ((gap)//2)+((gap)%2)

    for i in range(n):
        nums1[m+i] = nums2[i]


nums1 = [1,2,3,0,0,0] 
m = 3
nums2 = [2,5,6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)