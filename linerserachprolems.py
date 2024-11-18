class LinearSearchProblems:

    # search in the array: return index if found otherwise return -1
    def linear_search(self, arr, target):
        index = -1
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return index

    def linear_search_string(self, stringword:str, target: str):
         return stringword.find(target)
        # you can iterate over the loop as well

    def findinrage(self,arr, target, start,end):
        if len(arr) == 0: return -1
        for i in range(start,end+1):
            if arr[i] == target:
                return i
        return -1

 # list.index()-->this method is only for 1 D arry. if used in 2D array. need to pass target as a list
    def search2Darray(self, arr, target):
        for i in arr:
            for j in i:
                if j == target:
                    return True
        return False

    def max2Darry(self,arr):
        max = -2**31

        for i in arr:
            for j in i:
                if j > max:
                    max = j
        return max

    def findevenNumberCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # evencount = 0
        # for num in nums:
        #       if len(str(num))% 2 == 0 and num !=0:
        #           evencount+=1
        #
        # return evencount

        evencount = 0
        for num in nums:
            if self.even(num):
                evencount+=1

        return evencount

    def even(self, num):
        count = 0
        while num > 0:
            count+=1
            num//=10

        if count%2 == 0 and count != 0:
            return True
        return False









arr = [4,12,1,6,7,99,0,12,13,44]
obj = LinearSearchProblems()
# print(obj.linear_search(arr, 13))
# print(obj.linear_search_string("najmudin", 'd'))
# print(obj.findinrage("najmudin", 'a', 4, 7))

ary = [[1,2,3,4],[10.12,14,15],[11,22,33,44]]

# print(obj.search2Darray(ary,22))
# print(obj.max2Darry(ary))
print(obj.findevenNumberCount(arr))