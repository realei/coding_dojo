"""
Description:
Yes, using Python generator can reduce the space complexity of DFS preorder traversal to O(1). Normally, preorder traversal requires a stack to maintain the traversal order, resulting in a space complexity of O(h), where h is the height of the tree. However, by using generator, we can turn this stack into an implicit call stack, which reduces the space complexity to O(1).
"""


"""
Solution 1:
Space Complexity: O(h), `h` is the high of the tree
"""

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrderDFS(self, node: Optional[TreeNode]) -> List[int]:
            nonlocal res
            if node:
                res.append(node.val)
                preOrderDFS(node.left)
                preOrderDFS(node.right)

        preOrderDFS(root)

        return res


"""
Solution 2: Generator
Space Complexity: O(1)
"""
"""

from typing import  Generator, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preOrderGen(root: Optional[TreeNode]) -> Generator[int, None, None]:
            if root:
                yield root.val
                yield from preOrderGen(root.left)
                yield from preOrderGen(root.right)

        return list(preOrderGen(root))
