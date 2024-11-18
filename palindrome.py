class Palindrome:
    def isStringPalindrome(self, st):
        def checkPalindrome(st, i, length):
            # Base case: If we have checked all pairs or reached the middle
            if i >= length // 2:
                return True
            # If characters don't match
            if st[i] != st[length - i - 1]:
                return False
            # Recursive check for the next pair
            return checkPalindrome(st, i + 1, length)

        # Start recursion
        return checkPalindrome(st, 0, len(st))

    def is_palindrome(self, input_str):
        # Remove spaces and convert to lowercase for case-insensitive comparison
        cleaned_str = "".join(input_str.split()).lower()
        # Check if the cleaned string is the same as its reverse
        return cleaned_str == cleaned_str[::-1]
#
# class Solution:
#     # Complete this function
#     def ispalindrom(self, string_word):
#         start = 0
#         end = len(string_word)-1
#         return self.checkpalindrome(start,end,string_word)
#
#     def checkpalindrome(self,start, end, string_word):
#         if start>=end:
#             return True
#         if string_word[start] != string_word[end]:
#             return False
#         start+=1
#         end-=1
#         return self.checkpalindrome(start,end,string_word)
#
#
#
#
#
#
# obj = Solution()
# print(obj.ispalindrom("malayalam"))


if __name__ == "__main__":
    obj = Palindrome()
# print(obj.isStringPalindrome("madam"))
# print(obj.isStringPalindrome("najmudin"))
    print(obj.isstrpalindrom("   madam"))

