class Sorting:

    def mergeSort(self, arr):
        if len(arr) == 1:
            return arr

        # Split the array into two halves
        mid = len(arr)//2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])

        # Merge the sorted halves
        return self.merge(left,right)


    def merge(self, left, right):

        merged = []
        i = 0
        j = 0
        # Merge the two sorted lists
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        # Add any remaining elements from both halves
        if i < len(left):  #no need of these conditions
            merged.extend(left[i:])
        if j < len(right):
            merged.extend(right[j:])

        return merged

    # inline merge sort: without using extra space(array). this excees timelimit.
    # class Solution:
    #
    #     def mergeSort(self, arr, l, r):
    #         # code here
    #         if l >= r:
    #             return
    #
    #         # Find the middle point
    #         mid = l + (r - l) // 2
    #
    #         # Recursively sort first and second halves
    #         self.mergeSort(arr, l, mid)
    #         self.mergeSort(arr, mid + 1, r)
    #
    #         # Merge the sorted halves
    #         self.merge_in_place(arr, l, mid, r)
    #
    #     def merge_in_place(self, arr, l, mid, r):
    #         # Initialize pointers
    #         i = l
    #         j = mid + 1
    #
    #         # While there are elements in both halves
    #         while i <= mid and j <= r:
    #             if arr[i] <= arr[j]:
    #                 # Element at i is in the correct position
    #                 i += 1
    #             else:
    #                 # Element at j is smaller, needs to be inserted at i
    #                 temp = arr[j]
    #                 k = j
    #
    #                 # Shift all elements from i to j-1 one position to the right
    #                 while k > i:
    #                     arr[k] = arr[k - 1]
    #                     k -= 1
    #
    #                 # Place the element at i
    #                 arr[i] = temp
    #
    #                 # Update pointers
    #                 i += 1
    #                 mid += 1
    #                 j += 1

 # inplace, but use extra array

    # class Solution:
    #     def mergeSort(self, arr, l, r):
    #         if l >= r:
    #             return
    #
    #         # Find the middle point
    #         mid = l + (r - l) // 2
    #
    #         # Recursively sort first and second halves
    #         self.mergeSort(arr, l, mid)
    #         self.mergeSort(arr, mid + 1, r)
    #
    #         # Merge the sorted halves
    #         self.merge(arr, l, mid, r)
    #
    #     def merge(self, arr, l, mid, r):
    #         # Create temporary arrays for the two halves
    #         left = arr[l:mid + 1]
    #         right = arr[mid + 1:r + 1]
    #
    #         # Merge the two sorted halves
    #         i = 0  # Pointer for the left array
    #         j = 0  # Pointer for the right array
    #         k = l  # Pointer for the original array
    #
    #         while i < len(left) and j < len(right):
    #             if left[i] <= right[j]:
    #                 arr[k] = left[i]
    #                 i += 1
    #             else:
    #                 arr[k] = right[j]
    #                 j += 1
    #             k += 1
    #
    #         # Copy any remaining elements from the left array
    #         while i < len(left):
    #             arr[k] = left[i]
    #             i += 1
    #             k += 1
    #
    #         # Copy any remaining elements from the right array
    #         while j < len(right):
    #             arr[k] = right[j]
    #             j += 1
    #             k += 1

    # Example usage






















