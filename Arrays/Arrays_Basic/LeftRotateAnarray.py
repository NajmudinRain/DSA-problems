from collections import Counter
class Solution(object):
    # Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
    # Output:[4,5,6,7,1,2,3]

    def rotate_left(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #brute force
        """
        size = len(nums)
        k = k%size
        for _ in range(k):
            nums.insert(size,nums.pop(0))

        print(nums)
        """

        #better approach
        """ 
        size = len(nums)
        k = k%size
        temp = nums[:k]
        for i in range(k,size):
            nums[i-k] = nums[i]

        # t = 0
        for j in range(size-k, size):
            nums[j] = temp[j-(size-k)]
            # nums[j] = temp[t]
            # t+=1
        print(nums) 
        """

        # optimal approcah
        size = len(nums)

        k = k%size
        nums[:k] =nums[:k][::-1]
        nums[k:size] =nums[k:size][::-1]
        nums[:size] = nums[:size][::-1]
        print(nums)










obj = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
obj.rotate_left(nums, k)
