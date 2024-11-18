# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
# https://chatgpt.com/c/67701627-9ef0-800e-b503-ef78f36ff820
class Solution(object):
    def removeDuplicates(self, nums:list) -> None:
        """
        :type nums: List[int]
        :rtype: int
        """
        # brute-force approach
        temp_set = sorted(set(nums))
        index = 0
        for num in temp_set:
            nums[index] = num
            index+=1
        return index

        #optimal
    def removeDuplicates_Optimal(self, nums):
        #take two pointer i at 0 and j at 1. check for the element which is not equal to i and place it rght after i.
        i = 0
        for j in range(1,len(nums)):
            if nums[j]!= nums[i]:
                i+=1
                nums[i] = nums[j]
        return i + 1




