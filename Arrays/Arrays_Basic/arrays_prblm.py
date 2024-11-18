# 1. second largest element in an array

#brute-force: by sorting an array and getting the second largest element
#better-soln: find largest first by creating one function, then find second largest by creating another functoion. use largest val from first function
def second_largest_elem_arr(arr):
    largest = arr[0]
    sec_largest = -1 #suppose no negative num in array.if -ve is there say, -2**31 or use -float('inf') or float('inf')(for max_val)
    for i in range(1,len(arr)):
        if arr[i] > largest:
            largest,sec_largest = arr[i], largest
        elif arr[i] < largest and arr[i] >sec_largest:
            sec_largest = arr[i]

    print(sec_largest)

# second_largest_elem_arr([12,1,41,100,100,10])

# 2. check if array is sorted,

def if_sorted(arr):
    size = len(arr)
    if size<=1:
        return True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

# print(if_sorted([1,2,3,4,5]))

nums = [-1,0,0,0,0,3,3]
print(set(nums))



