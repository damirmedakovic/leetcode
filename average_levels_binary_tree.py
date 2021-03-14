# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        
        
        levels_avg = []
        thislevel = [root]
        while thislevel: 
            nextlevel = list()
            level_sum = 0 
            level_counter = 0
            for n in thislevel:
                level_counter += 1.0
                level_sum += n.val
                if n.left: nextlevel.append(n.left)
                if n.right: nextlevel.append(n.right)
            
            levels_avg.append(level_sum/level_counter)
            thislevel = nextlevel
        return levels_avg
