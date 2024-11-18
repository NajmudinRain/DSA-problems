class BinarySearch:
    def binarysearch(self, arr, target):
        start = 0
        end = len(arr)-1
        while start<=end:
            mid = start + (end - start)//2
            if target >arr[mid]:
                start = mid + 1
            elif target < arr[mid]:
                end = mid - 1
            else:
                return mid
        return -1

    def orderAgnosticBS(self, arr, target):
        start = 0
        end = len(arr) - 1
        # is_asc = arr[start] < arr[end] this will be index out of bound in case of empty list,arr. so better right this condt after while
        while start<=end:
            mid = start + (end-start)//2
            if target == arr[mid]:
                return mid
            if arr[start] < arr[end]:
                if target > arr[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if target > arr[mid]:
                    end = mid -1
                else:
                    start = mid + 1

        return -1



obj = BinarySearch()
arr = [11, 13, 15,16,17,18,19,21,22,23,25,26,28]
print(obj.binarysearch([],19))

# print(obj.orderAgnosticBS(arr,15))