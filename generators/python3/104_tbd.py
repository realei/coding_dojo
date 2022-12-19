# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfsMaxGen(node: Optional[TreeNode]) -> Generator[int, None, None]:
            depth = 0
            if root:
                depth += 1
                yield from dfsMaxGen(root.left)
                yield from dfsMaxGen(root.right)
            else:
                yield depth

        res = 0
        for val in dfsMaxGen(root):
            print(val)
            res = max(res, val)
        
        return res
