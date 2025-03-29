# https://neetcode.io/problems/is-palindrome

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(lambda x : (ord(x)<=ord('z') and ord(x)>=ord('A')) or (ord(x)>=ord('0') and ord(x)<=ord('9')), ''.join(s.split(' '))))
        n = len(s)
        s = ''.join(s).lower()
        for i in range(len(s)//2):
            if s[i] != s[n-i-1]:
                return False
        return True

# time complexity: O(n)
# space complexity: O(n)