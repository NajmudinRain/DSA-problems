class Solution:

    def bs_recurr(self, arr,start, end, k):
        if end < start:
            return -1
        mid = start + (end-start)//2
        if arr[mid] == k:
            return mid
        if arr[mid] > k:
            return self.bs_recurr(arr,start, mid-1, k)
        return self.bs_recurr(arr,mid+1, end, k)


obj = Solution()
arr = [1,2,3,7,9,11,20]
print(obj.bs_recurr([1,2,3,7,9,11,20],0,len(arr)-1, 4))

