#consider the array here ot be infinitive. use of len() function is not allowed for this question.
from re import search


class InfiniteArraySearch:

    def searchtarget(self, arr, target):
        start = 0
        if len(arr) > 1:
            end = 1

        while target > arr[end]:
            # start = end + 1
            # end = 2 * end
            temp = end + 1
            end = end + (end - start + 1) * 2
            start = temp

        ans = self.search(arr, target, start, end)

        return ans

    def search(self, arr, target, start , end):

        while(start<=end):
            mid = start + (end - start)//2

            if target == arr[mid]:
                return mid
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


obj = InfiniteArraySearch()
print(obj.searchtarget([2, 4,6,11,14,15,17], 14))