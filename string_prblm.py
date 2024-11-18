def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    # return " ".join(reversed(s.strip().split()))

    # return " ".join(s.strip().split()[::-1])
sorted()
    i = 0
    n = len(s)
    result = ""
    while (i < n):

        while (i < n and s[i] == " "):
            i += 1
        j = i
        while (j < n and s[j] != " "):
            j += 1
        word = s[i:j]
        if result and i != j:
            result = word + " " + result
        else:
            result = word
        i = j

    return result

print(reverseWords("  hello world  "))