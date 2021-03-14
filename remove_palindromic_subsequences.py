class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        
        return 2 - (s== s[::-1]) - (s == "")
