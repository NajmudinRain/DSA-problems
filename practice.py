from distutils.command.check import check


class Solution:
    # Complete this function
    def ispalindrom(self, string_word):
        start = 0
        end = len(string_word)-1
        return self.checkpalindrome(start,end,string_word)

    def checkpalindrome(self,start, end, string_word):
        if start>=end:
            return True
        if string_word[start] != string_word[end]:
            return False
        start+=1
        end-=1
        return self.checkpalindrome(start,end,string_word)






obj = Solution()
print(obj.ispalindrom("malayalam"))
