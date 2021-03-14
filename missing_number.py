class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        sum_formula = len(nums) *((len(nums) + 1))/2
        sum_real = 0
        for i in nums:
            sum_real += i
            
        return sum_formula - sum_real
        
