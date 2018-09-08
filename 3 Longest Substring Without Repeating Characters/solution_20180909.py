class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        start = 0
        end = 1
        if len(s) <= 1:
            return len(s)
        else:
            while True:
                string = s[start:end]
                l = len(string)
                if end < len(s):
                    if s[end] not in string:
                        end += 1
                        l += 1
                        if max_length < l:
                            max_length = l
                    else:
                        start += 1
                        
                else:
                    return max_length