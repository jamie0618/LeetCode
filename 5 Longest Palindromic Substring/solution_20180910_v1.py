class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """       
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return s
        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        else:
            max_string = s[0]
            for i in range(1, len(s)-1):
                odd = self.CheckOdd(s, i)
                even = self.CheckEven(s, i)
                if len(odd) > len(even) and len(odd) > len(max_string):
                    max_string = odd
                elif len(odd) < len(even) and len(even) > len(max_string):
                    max_string = even
            return max_string
            
    def CheckOdd(self, s, i):
        start = 1
        end = 1
        return self.Check(s, i, start, end)
    
    def CheckEven(self, s, i):
        if s[i] == s[i-1]:
            start = 2
            end = 1
            return self.Check(s, i, start, end)
        elif s[i] == s[i+1]:
            start = 1
            end = 2
            return self.Check(s, i, start, end)
        else:
            return s[i]

    def Check(self, s, i, start, end):
        while i-start >= 0 and i+end < len(s):
            if s[i-start] != s[i+end]:
                return s[i-start+1:i+end]
            else:
                start += 1
                end += 1
        return s[i-start+1:i+end]