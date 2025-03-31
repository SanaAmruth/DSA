# https://neetcode.io/problems/generate-parentheses


class Solution:
    def __init__(self,):
        self.perms = []
    def permutes(self, freq, result, n_left, n_right, n):
        if n_right>n_left:
            return
        if len(result) == 2*n:
            self.perms.append(''.join(result))
        for i in freq:
            if freq[i] > 0:
                freq[i] -= 1
                result.append(i)
                self.permutes(freq, result, n_left+(i=='('), n_right+(i==')'), n)
                freq[i] += 1
                result.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        freq = {'(':n, ')':n}
        self.permutes(freq, [], 0, 0, n)
        return self.perms

# Time Complexity: O(4^n/sqrt(n))
# Space Complexity: O(n)