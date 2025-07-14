def XOR(nums):
    xr = 0
    for i in range(len(nums)):
        xr = xr ^ (i+1) ^ nums[i]
    
    # bitno = xr & ~(xr-1)

    bitno = 0

    while True:
        if xr & (1 << bitno) == 1:
            break
        bitno+=1
    
    zero = 0
    one = 0

    for i in range(len(nums)):
        if nums[i] & (1<<bitno) == 1:
            one ^= nums[i]
        else:
            zero ^= nums[i]

        if (i+1) & (1<<bitno) == 1:
            one ^= (i+1)
        else:
            zero ^= (i+1)
    return [zero , one] if zero in nums else [one,zero]

def Maths(nums):
    val1 = 0 
    val2 = 0

    for i in range(len(nums)):
        val1 += (nums[i] - (i+1))
        val2 += ((nums[i]**2) - ((i+1)**2))

    val2 = val2//val1
    x = (val2 + val1)//2
    y = val2 - x
    
    return [x,y]
    



nums = [3, 5, 4, 1, 1]
print(Maths(nums))

