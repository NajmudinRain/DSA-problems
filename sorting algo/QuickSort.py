class Solution:
    # Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)

    def partition(self, arr, low, high):
        # code here
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

arr = [2, 27, 43, 3, 9, 82, 1]
solution = Solution()
solution.quickSort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)


# class Solution:
    # Function to sort a list using quick sort algorithm.

    # def quickSort(self, arr, low, high):
    #     if low < high:
    #         # Partition the array and get the pivot index
    #         pindex = self.partition(arr, low, high)
    #         # Recursively sort elements before and after partition
    #         self.quickSort(arr, low, pindex - 1)
    #         self.quickSort(arr, pindex + 1, high)
    #
    # def partition(self, arr, low, high):
    #     # Choose the middle element as pivot
    #     mid = low + (high - low) // 2
    #     pivot = arr[mid]
    #
    #     # Initialize pointers
    #     i = low
    #     j = high
    #     # Partition the array around the pivot
    #     while i <= j:
    #         # Find elements on the wrong side of the pivot
    #         while arr[i] < pivot:
    #             i += 1
    #         while arr[j] > pivot:
    #             j -= 1
    #
    #         # Swap elements if necessary
    #         if i <= j:
    #             arr[i], arr[j] = arr[j], arr[i]
    #             i += 1
    #             j -= 1
    #     # Return the partition index (where the pivot should ideally be)
    #     return i
#
# # Example usage
#     8,9,1,2,3,4
# arr = [38, 27, 43, 3, 9, 82, 10]
# arr = [2, 27, 43, 3, 9, 82, 1]
# solution = Solution()
# solution.quickSort(arr, 0, len(arr) - 1)
# print("Sorted Array:", arr)



# using auxillary space
# def quick_sort(arr):
#     # Base case: A list of 0 or 1 elements is already sorted
#     if len(arr) <= 1:
#         return arr
#
#     # Choose the pivot (typically the last element or any other strategy)
#     pivot = arr[-1]
#
#     # Partition the array into three parts:
#     # Elements less than the pivot
#     left = [x for x in arr[:-1] if x <= pivot]
#     # Elements equal to the pivot
#     middle = [pivot]
#     # Elements greater than the pivot
#     right = [x for x in arr[:-1] if x > pivot]
#
#     # Recursively sort the left and right parts, then combine
#     return quick_sort(left) + middle + quick_sort(right)
#




# # Example usage
# arr = [38, 27, 43, 3, 9, 82, 10]
# sorted_arr = quick_sort(arr)
# print("Sorted Array:", sorted_arr)
