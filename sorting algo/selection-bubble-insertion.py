# class Solution:
#     def selectionSort(self, arr):
#         n = len(arr)
#         for i in range(n - 1):  # Stop at n-1
#             min_index = i
#             for j in range(i + 1, n):
#                 if arr[j] < arr[min_index]:
#                     min_index = j
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#
#     def bubbleSort(self, arr):
#         # code here
#         # [8, 3 ,6,5,4,1,2]
#         # for i in range(len(arr)):
#         #     swapped = False
#         #     for j in range(len(arr)- i -1):
#         #         if arr[j] > arr[j + 1]:
#         #             arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         #             swapped = True
#         #     if not swapped:
#         #         break
#
#         for i in range(len(arr) - 1, 0, -1):
#             swapped = False
#             for j in range(i):
#                 if arr[j] > arr[j + 1]:
#                     arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                     swapped = True
#             if not swapped:
#                 break
#
#     def insertionSort(self, arr):
#         # code here
#         # [5 4,1,2,8,0]
#         for i in range(len(arr)):
#             j = i
#             while (j > 0 and arr[j] < arr[j - 1]):
#                 arr[j], arr[j - 1] = arr[j - 1], arr[j]
#                 j -= 1

def mergeSort(arr):
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)
def merge(left, right):
     i,j = 0, 0
     m = len(left)
     n = len(right)
     result = []
     while i < m and j < n:
         if left[i] < right[j]:
             result.append(left[i])
             i+=1
         else:
             result.append(right[j])
             j+=1
     while i < m:
        result.append(left[i])
        i+=1
     while j < n:
        result.append(right[j])
        j+=1

     return result


print(mergeSort([6,5,4,3,2,1]))




















