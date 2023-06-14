# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            """
            inOrder Traversal
            """
            if node:
                yield from dfs(node.left)
                yield node.val
                yield from dfs(node.right)
        
        bst_gen = dfs(root)
        prev = next(bst_gen)
        min_val = 1e9
        for val in bst_gen:
            min_val = min(min_val, val - prev)
            prev = val

        return min_val

