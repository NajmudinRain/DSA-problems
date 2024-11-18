# https://www.geeksforgeeks.org/problems/count-number-of-substrings4528/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=count-number-of-substrings


class Solution:
    def countSubstr(self, s, k):
        """
        Counts the number of substrings with exactly k distinct characters.

        Args:
            s: The input string.
            k: The desired number of distinct characters.

        Returns:
            The total count of substrings.
        """

        def atMostk(s, k):
            """
            Counts the number of substrings with at most k distinct characters.
            """
            start = 0
            count = 0
            freq = {}
            for end in range(len(s)):
                freq[s[end]] = freq.get(s[end], 0) + 1
                while len(freq) > k:
                    freq[s[start]] -= 1
                    if freq[s[start]] == 0:
                        del freq[s[start]]
                    start += 1
                count += end - start + 1  # Count all substrings ending at 'end'
            return count

        return atMostk(s, k) - atMostk(s, k - 1)

obj = Solution()
print(obj.countSubstr("abaaca",1))