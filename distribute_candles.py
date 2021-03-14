class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        amount = len(candyType) / 2
        unique = len(set(candyType))
        
        if unique >= amount: 
            return amount
        else:
            return unique
