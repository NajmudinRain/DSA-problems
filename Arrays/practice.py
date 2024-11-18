class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # brute-force
        # pos_nums = []
        # neg_nums = []
        # result = []
        # for num in nums:
        #     if num > 0:
        #         pos_nums.append(num)
        #     else:
        #         neg_nums.append(num)
        # for i in range(len(pos_nums)):
        #     result.append(pos_nums[i])
        #     result.append(neg_nums[i])

        # return result

        # better:
        # i = 0
        # j = 1
        # result=[0] * len(nums)
        # for num in nums:
        #     if num > 0:
        #         result[i] = num
        #         i+=2
        #     else:
        #         result[j] = num
        #         j+=2
        # return result

        # optimal
        pos_index = 0
        neg_index = 1
        while (pos_index < len(nums) and neg_index < len(nums)):
            while (pos_index < len(nums) and nums[pos_index] >= 0):
                pos_index += 2

            while (neg_index < len(nums) and nums[neg_index] <= 0):
                neg_index += 2

            if (pos_index < len(nums) and neg_index < len(nums)):
                nums[pos_index], nums[neg_index] = nums[neg_index], nums[pos_index]

        return nums


obj = Solution()
nums = [28,-41,22,-8,-37,46,35,-9,18,-6,19,-26,-37,-10,-9,15,14,31]
obj.rearrangeArray(nums)
print(nums)




