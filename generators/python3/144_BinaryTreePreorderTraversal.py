# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import  Generator, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrderGen(root: Optional[TreeNode]) -> Generator[int, None, None]:
            if root:
                yield root.val
                yield from preOrderGen(root.left)
                yield from preOrderGen(root.right)

        return list(preOrderGen(root))
