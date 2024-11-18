# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # done with your own thought process.
        #  6 5 4 3 2 1 0
        # 1 2 3 4 5 6
        #   4 5 6 7 0 1 2 3
        # 6 6 6 6 9
        #  1 2 3 4 4 4 4
        # 1 1 0 44444
        #        4 4 4 1 0 4 4
        # peak = self.findPivot(nums)
        # peak = self.findPivotwithDuplicate(nums)
        peak = self.findPivot(nums)
        start = 0
        end = len(nums) - 1
        ans = self.binarysearch(nums, target, start, peak)
        if ans == -1:
            ans = self.binarysearch(nums, target, peak + 1, end)

        return ans

    def findPivot(self, arr):
        start = 0
        end = len(arr) - 1
        while (start <= end):
            mid = start + (end - start) // 2

            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            elif mid > start and arr[mid] < arr[mid - 1]:
                return mid - 1
            elif arr[start] > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1

        return - 1

    def binarysearch(self, arr, target, start, end):
        while (start <= end):
            mid = start + (end - start) // 2

            if target < arr[mid]:
                end = mid - 1
            elif target > arr[mid]:
                start = mid + 1
            else:
                return mid

        return -1

#
    def findPivotwithDuplicate(self, arr):
        start = 0
        end = len(arr) - 1
        while (start <= end):
            mid = start + (end - start) // 2

            if mid < end and arr[mid] > arr[mid + 1]:
                return mid
            elif mid > start and arr[mid] < arr[mid - 1]:
                return mid - 1
            elif arr[start] == arr[mid] and arr[mid] == arr[end]:
                if start < end and arr[start] > arr[start + 1]:
                    return start
                start += 1
                if end > start and arr[end] < arr[end - 1]:
                    return end -1
                end -= 1
            elif arr[start] <= arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

        return - 1



    def findarrayrotationcount(self, arr):
        pivot = self. findPivot(arr)
        return pivot + 1

obj = Solution()
# print(obj.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1],2))
print(obj.findarrayrotationcount([1,2,3,5]))
