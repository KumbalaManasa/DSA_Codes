#Optimal Approach
#TC = O(N) SC = O(1)
def issorted(arr):
    for i in range(1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True
arr = [1,2,3,4,5]
print(issorted(arr))    

#Better Approach
#TC = O(N^2) SC = O(1)
'''def check_if_arr_sorted(arr):
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[j]<arr[i]:
                    return False
        return True
    arr = [1, 2, 3, 4, 5]
    print(check_if_arr_sorted(arr))'''    