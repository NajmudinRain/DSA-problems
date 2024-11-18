# ceiling of the number: the smallest of the given number which is just greater or equal to the num
#   0 1  2  3  4  5
# [11,13,15,16,18,20]
class BSQuestions:

    #return the ceiling of the number
    def ceilingofNumber(self, arr, target):
        if target > arr[len(arr) - 1]:
            return -1  # Ceiling doesn't exist
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                return mid  # Exact match
        return start  # Index of the smallest number >= target

    def floorofNumber(self, arr, target):
        if target < arr[0]:
            return -1  # Floor doesn't exist
        start = 0
        end = len(arr) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if target > arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                return mid  # Exact match
        return end  # Index of the largest number <= target


obj = BSQuestions()
arr = [2,4,5,6,7, 8 , 10]
# obj.ceilingofNumber(arr,8 )
print(obj.floorofNumber(arr,1 ))
