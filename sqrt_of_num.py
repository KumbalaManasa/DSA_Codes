#optimal approach
def sqrt_num(num):
    low = 0
    high = num
    ans = 0
    while low<=high:
        mid = (low+high)//2
        if mid*mid == num:
            ans = mid
            return ans
        elif mid*mid < num:
            low = mid+1
        else:
            high = mid-1   
print(sqrt_num(36))             

'''#brute force TC = O(N) SC = O(1)
def sqrt_num(num):
    ans = 0
    for i in range(1,num+1):
        if i*i<=num:
            ans = i
        else:
            break    
    return ans  
print(sqrt_num(25)) '''     
