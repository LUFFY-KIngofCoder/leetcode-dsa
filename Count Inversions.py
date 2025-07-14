def ms(nums,l , r):
    count = 0
    if l == r:
        return count
    mid = (l+r)//2
    count += ms(nums , l , mid)
    count += ms(nums, mid+1 , r)
    count += merge(nums , l , mid , r)
    return count

def merge(nums , l , mid, r):   
    i = l
    j = mid+1
    temp=[]
    count = 0
    while i <= mid and j <= r:
        if nums[i] <= nums[j]:
            temp.append(nums[i])
            i+=1
        else:
            temp.append(nums[j])
            count += mid - i +1
            j+=1
    
    while i <= mid:
        temp.append(nums[i])
        i+=1
        
    while j <= r:
        temp.append(nums[j])
        j+=1

    for i in range(len(temp)):
        nums[l+i] = temp[i]

    return count
        
# def counter(nums , l , mid, r, count):
#     i = l
#     j = mid+1
#     while i < mid+1 and j <= r:
        
#         if nums[i] > nums[j]:
#             count += mid - i + 1
#             j+= 1
#         else:
#             i+=1
        
#     return count

def numberOfInversions(nums):
    return ms(nums,0,len(nums)-1)

nums = [2, 3, 7, 1, 3, 5]
print(numberOfInversions(nums))

    





#--------------------------------------------------------------
# def ms(nums,l , r , count):
#     if l == r:
#         return 
#     mid = (l+r)//2
#     ms(nums , l , mid , count)
#     ms(nums, mid+1 , r , count)
#     count = counter(nums , l ,mid , r, count)
  
#     merge(nums , l , mid , r)

#     return count

# def merge(nums , l , mid, r):   
#     i = l
#     j = mid+1
#     temp=[]
#     while i <= mid and j <= r:
#         if nums[i] <= nums[j]:
#             temp.append(nums[i])
#             i+=1
#         else:
#             temp.append(nums[j])
#             j+=1
    
#     while i <= mid:
#         temp.append(nums[i])
#         i+=1
        
#     while j <= r:
#         temp.append(nums[j])
#         j+=1

#     for i in range(len(temp)):
#         nums[l+i] = temp[i]
        
# def counter(nums , l , mid, r, count):
#     i = l
#     j = mid+1
#     while i < mid+1 and j <= r:
        
#         if nums[i] > nums[j]:
#             count += mid - i + 1
#             j+= 1
#         else:
#             i+=1
        
#     return count

# def numberOfInversions(nums):
#     return ms(nums,0,len(nums)-1 , 0)

# nums = [2, 3, 7, 1, 3, 5]
# print(numberOfInversions(nums))




    