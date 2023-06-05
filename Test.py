from collections import Counter
def firstUniqChar(s):
        hash = Counter(s)
        for i in range(len(s)):
            if hash.get(s[i])==1:
                return i
        return -1
print(firstUniqChar('leetcode'))